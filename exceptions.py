"""
Module định nghĩa các Custom Exception của ứng dụng.
"""

class InvalidCurrencyError(Exception):
    """Ném ra khi mã tiền tệ không tồn tại trong hệ thống."""
    pass

class NegativeAmountError(Exception):
    """Ném ra khi số tiền nhập vào nhỏ hơn 0."""
    pass