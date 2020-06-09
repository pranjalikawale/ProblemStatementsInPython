import pytest
from user_registeration import UserRegisteration
from validation_exception import ValidationException


class TestValidation:
    def test_pass_when_valid_name_given(self,user_registeration_object):
        user_registeration_object.check_name_validation("Pranjali")
    
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
        user_registeration_object.check_email_validation("abc.s@gmail.com")
    
    def test_pass_when_invalid_email_given_throws_exception(self,user_registeration_object):
        with pytest.raises(ValidationException) as exception:
            user_registeration_object.check_email_validation("abc.1#2@bridgelabzgmail.com")
        assert str(exception.value)=="Invalid Email Address"

    def test_pass_when_valid_password_with_length_eight_character_given(self,user_registeration_object):
        user_registeration_object.check_password_validation("Pran1234")

    def test_pass_when_valid_password_having_atleast_one_uppercase_given(self,user_registeration_object):
        user_registeration_object.check_password_validation("Pran1234")

    def test_pass_when_valid_password_having_atleast_one_digit_given(self,user_registeration_object):
        user_registeration_object.check_password_validation("Prajali1")

    def test_pass_when_valid_password_having_exactly_one_symbol_given(self,user_registeration_object):
        user_registeration_object.check_password_validation("Prajali1@")
    
    def test_pass_when_invalid_password_given_throws_exception(self,user_registeration_object):
        with pytest.raises(ValidationException) as exception:
            user_registeration_object.check_password_validation("pran123#@")
        assert str(exception.value)=="Invalid Password"
    



