def calculate_position_size(
    balance,
    risk_percent,
    entry,
    stop_loss
):

    risk_amount = balance * risk_percent

    difference = abs(entry - stop_loss)

    if difference == 0:
        return 0

    size = risk_amount / difference

    return round(size, 4)