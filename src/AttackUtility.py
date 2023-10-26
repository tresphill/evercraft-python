from src.AttackStatus import AttackStatus

class AttackUtility:

    def eval_attack(opponent, attack_value):
        # needs to return an attack status
        # need opponents armor class
        # if attack value = 20 automatic critical
        if (attack_value == 20):
            return AttackStatus.CRITICAL
        # if attack value >= opp armor class
        if (attack_value >= opponent.armor_class):
            return AttackStatus.HIT

        return AttackStatus.MISS