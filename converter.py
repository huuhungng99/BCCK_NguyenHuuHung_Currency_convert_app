from config import RATES
from exceptions import InvalidCurrencyError, NegativeAmountError

def convert_currency(amount, src, dst):
    """Hàm thuần logic: chuyển đổi tiền tệ và trả về kết quả."""
    if amount < 0:
        raise NegativeAmountError("Số tiền không được âm!")
        
    src = src.upper().strip()
    dst = dst.upper().strip()
    
    if src not in RATES:
        raise InvalidCurrencyError(f"Mã gốc không hỗ trợ: {src}")
    if dst not in RATES:
        raise InvalidCurrencyError(f"Mã đích không hỗ trợ: {dst}")
        
    return (amount / RATES[src]) * RATES[dst]