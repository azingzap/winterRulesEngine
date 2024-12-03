import json

#This file contains the functions for the rule engine.

def rulesEngine(familyComposition, numberOfChildren):
    '''
    This function accepts the following parameters:
    familyComposition - a string that represents the family composition and can be single or a couple.
    numberOfChildren - an integer that represents the number of children the family composition has.
    Using these parameters the function determines how much winter supplement a client will receive.

    This function acts as the rules engine and determines how much winter supplement a client will receive.

    The function returns three values:
    baseAmountValue - a float that represents how much money the client will get based on its marital status.
    childrenAmountValue - a float that represents how much money the client will get based on how many kids they have.
    supplementAmountValue - a float that represents the total amount of money they will receive.
    '''

    if numberOfChildren < 0:
        raise Exception("You can't have a negative amount of kids")
        #raise Exception("Invalid email address")

    if familyComposition != "single" and familyComposition != "couple":
        raise Exception("Your family composition must be 'single' or 'couple'")

    baseAmountValue = 0
    childrenAmountValue = 0
    supplementAmountValue = 0

    if familyComposition == "couple" and numberOfChildren == 0:
        baseAmountValue = 120
        supplementAmountValue = baseAmountValue + childrenAmountValue

    elif familyComposition == "single" and numberOfChildren == 0:
        baseAmountValue = 60
        supplementAmountValue = baseAmountValue + childrenAmountValue

    elif (familyComposition == "couple" or familyComposition == "single") and numberOfChildren >= 1:
         baseAmountValue = 120
         childrenAmountValue = 20 * numberOfChildren
         supplementAmountValue = baseAmountValue + childrenAmountValue

    return float(baseAmountValue), float(childrenAmountValue), float(supplementAmountValue)


def implementRulesEngine(message):
    '''
    This function accepts one parameter:
    message - a Json formatted string that represents a message from a client.

    This function determines if a government affiliated client is eligible for winter benefits. This function also
    implements the rules engine function to the message published from the Winter Application client.

    This function returns:
    a new message with the values generated from the rules engine function in a Json formatted string.
    '''

    key = json.loads(message)
    if key["familyUnitInPayForDecember"] == "true" or key["familyUnitInPayForDecember"] == "True":
        try:
            baseAmountValue, childrenAmountValue, supplementAmountValue = rulesEngine(str(key["familyComposition"]),int(key["numberOfChildren"]))
            return json.dumps({"id": str(key["id"]), "isEligible": str(key["familyUnitInPayForDecember"]),
                               "baseAmount": baseAmountValue, "childrenAmount": childrenAmountValue,
                               "supplementAmount": supplementAmountValue})
        except Exception as e:
            print("An exception occurred:", e)

    else:
        return json.dumps({"id":str(key["id"]),"isEligible": str(key["familyUnitInPayForDecember"]),"baseAmount":0.0,"childrenAmount": 0.0,"supplementAmount":0.0})
