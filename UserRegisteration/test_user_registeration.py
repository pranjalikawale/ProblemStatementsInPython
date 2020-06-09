import pytest
from user_registeration import UserRegisteration
from validation_exception import ValidationException


class TestValidation:
    def test_pass_when_valid_name_given(self,user_registeration_object):
        assert user_registeration_object.check_name_validation("Pranjali")==True
    
    def test_pass_when_invalid_name_given_throws_exception(self,user_registeration_object):
        with pytest.raises(ValidationException) as exception:
            user_registeration_object.check_name_validation("pranjali")
        assert str(exception.value)=="Invalid Name"

    def test_pass_when_valid_mobile_given(self,user_registeration_object):
        user_registeration_object.check_mobile_validation("91 2345678901")
    
    def test_pass_when_invalid_mobile_given_throws_exception(self,user_registeration_object):
        with pytest.raises(ValidationException) as exception:
            user_registeration_object.check_mobile_validation("9145678901")
        assert str(exception.value)=="Invalid Mobile Number"

    def test_pass_when_valid_email_given(self,user_registeration_object):
        assert user_registeration_object.check_email_validation("abc.s@gmail.com")==True
    
    def test_pass_when_invalid_email_given_throws_exception(self,user_registeration_object):
        with pytest.raises(ValidationException) as exception:
            user_registeration_object.check_email_validation("abc.1#2@bridgelabzgmail.com")
        assert str(exception.value)=="Invalid Email Address"

    def test_pass_when_valid_password_with_length_eight_character_given(self,user_registeration_object):
        assert user_registeration_object.check_password_validation("Pran1234")==True

    def test_pass_when_valid_password_having_atleast_one_uppercase_given(self,user_registeration_object):
        assert user_registeration_object.check_password_validation("Pran1234")==True

    def test_pass_when_valid_password_having_atleast_one_digit_given(self,user_registeration_object):
        assert user_registeration_object.check_password_validation("Prajali1")==True

    def test_pass_when_valid_password_having_exactly_one_symbol_given(self,user_registeration_object):
        assert user_registeration_object.check_password_validation("Prajali1@")==True
    
    def test_pass_when_invalid_password_given_throws_exception(self,user_registeration_object):
        with pytest.raises(ValidationException) as exception:
            user_registeration_object.check_password_validation("pran123#@")
        assert str(exception.value)=="Invalid Password"

    @pytest.mark.parametrize("input_data, result",[
            ("abc", "Invalid Email Address"),
            ("abc@.com.my", "Invalid Email Address"),
            ("abc123@gmail.a","Invalid Email Address"),
            ("abc123@.com","Invalid Email Address"),
            ("abc123@.com.com","Invalid Email Address"),
            (".abc@abc.com","Invalid Email Address"),
            ("abc()*@gmail.com","Invalid Email Address"),
            ("abc@%*.com","Invalid Email Address"),
            ("abc..2002@gmail.com","Invalid Email Address"),
            ("abc.@gmail.com","Invalid Email Address"),
            ("abc@abc@gmail.com","Invalid Email Address"),
            ("abc@gmail.com.1a", "Invalid Email Address"),
            ("abc@gmail.com.aa.au","Invalid Email Address"),  
    ])
    def test_pass_when_given_email_invalid_returns_result(self,user_registeration_object,input_data, result):
        with pytest.raises(ValidationException) as exception:
            user_registeration_object.check_email_validation(input_data)
        assert str(exception.value)==result

    @pytest.mark.parametrize("input_data, result",[
        ("abc@yahoo.com", True),
        ("abc-100@yahoo.com", True),
        ("abc.100@yahoo.com", True),
        ("abc111@abc.com", True),
        ("abc-100@abc.net", True),
        ("abc.100@abc.com.au", True),
        ("abc@1.com", True),
        ("abc@gmail.com", True),
        ("abc+100@gmail.com", True),  
    ])
    def test_pass_when_given_email_valid_returns_result(self,user_registeration_object,input_data, result):
            assert user_registeration_object.check_email_validation(input_data)==result
            



