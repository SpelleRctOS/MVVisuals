import random
import pickle
import json
import os
import datetime


print("MVVisuals(alfa v. 0.1)\n"
      "made by _SpelleR_\n"
      ""
      "")
# character stats
nmst = ["HP", "ATK", "ACC", "EXP"]
#lvlst = ["20", "5", "3"]
hHP = 30
hATK = 5
hACC = 3
exp = [0]
coin = []
inventory = []
merchantInventory = []


f = open('expdata.json')
exp = json.load(f)

g = open('HPdata_test.json')
hHP = json.load(g)

i = open('inventorydata.json')
inventory = json.load(i)

c = open('coindata.json')
coin = json.load(c)

mi = open('merchantInvdata.json')
merchantInventory = json.load(mi)


print(nmst[0], hHP)
print(nmst[1], hATK)
print(nmst[2], hACC)
#print(nmst[3], hSP) must be SP 8
print(nmst[3], sum(exp),"\n--------------------------")

# enemies stats
enemies = ["slime", "wolf"]
enemyst = ["HP", "ATK"]
slime = 1
slimeHP = 3
slimeATK = 1
# print(enemyst[0] ,slimelvl[0])
# print(enemyst [1],slimelvl[1])
wolf = 2
wolfHP = 10
wolfATK = 7
# print(enemyst[0] ,wolflvl[0])
# print(enemyst [1],wolflvl[1])

game = 'Y'
shop = 'enter'
time = datetime.datetime.today()
restore_merch_time = time.hour


if restore_merch_time == 0 or restore_merch_time == 3 or restore_merch_time == 6 or restore_merch_time == 9 or restore_merch_time == 12 or restore_merch_time == 15 or restore_merch_time == 18 or restore_merch_time == 21:
        merchantItems = ["Jelly", "Pink jelly", "Wolf's meat","Wolf's heart"]
        merchantItems_count = [5, 2, 4, 1]
        merchantInventory = sum([[s] * n for s, n in zip(merchantItems, merchantItems_count)], [])
        with open('merchantInvdata.json', 'w') as i:
            json.dump(merchantInventory, i)
        with open('file_merchantInventory', 'wb') as fi:
            pickle.dump(merchantInventory, fi)

while game == 'Y':
# Actions
    print("--------------------------")
    print("Type 1 to open inventory")
    print("Type 2 to show your balance")
    print("Type 3 to enter the shop")
    print("Type 4 to find an enemy")
    print("Type 0 to exit\n--------------------------")
    string = int(input())

# Inventory
    if string == 1:
        print("Your inventory:")
        #Counting elements in list - list_name.count(x))
        print("Jelly:",inventory.count("Jelly"),"Pink jelly:",inventory.count("Pink jelly"),"Wolf's meat:",inventory.count("Wolf's meat"),"Wolf's heart:",inventory.count("Wolf's heart"))
        print('--------------------------')
        print("Do you want to use anything? (y/n)\n--------------------------")
        inventoryChoise = input()
        if inventoryChoise == 'y':
            print("Choose what to use:\nJelly - 1; Pink jelly -2; Wolf's meat - 3; Wolf's heart - 4")
            healChoise = int(input())
            if healChoise == 1:
                if "Jelly" in inventory:

                    inventory.remove("Jelly")
                    with open('inventorydata.json', 'w') as i:
                        json.dump(inventory, i)

                    with open('file_slimeInventory', 'wb') as fi:
                        pickle.dump(inventory, fi)
                    print("You used an Jelly")
                    print("Your HP now is:", hHP + 2,"\n--------------------------")
                    hHP = hHP + 2
                    with open('HPdata_test.json', "w") as g:
                        json.dump(hHP, g)
                    with open('file_HP', 'wb') as fh:
                        pickle.dump(hHP, fh)
                else:
                    print("You do not have any Jelly\n--------------------------")

            if healChoise == 2:
                if "Pink jelly" in inventory:
                    inventory.remove("Pink jelly")
                    with open('inventorydata.json', 'w') as i:
                        json.dump(inventory, i)

                    with open('file_slimeInventory', 'wb') as fi:
                        pickle.dump(inventory, fi)
                    print("You used a Pink jelly")
                    print("Your HP now is:", hHP + 5,"\n--------------------------")
                    hHP = hHP + 5

                    with open('HPdata_test.json', "w") as g:
                        json.dump(hHP, g)
                    with open('file_HP', 'wb') as fh:
                        pickle.dump(hHP, fh)
                else:
                    print("You do not have any Pink jelly\n--------------------------")

            if healChoise == 3:
                if "Wolf's meat" in inventory:
                    inventory.remove("Wolf's meat")
                    with open('inventorydata.json', 'w') as i:
                        json.dump(inventory, i)

                    with open('file_wolfInventory', 'wb') as fi:
                        pickle.dump(inventory, fi)
                    print("You used a Wolf's meat")
                    print("Your HP now is:", hHP + 7,"\n--------------------------")
                    hHP = hHP + 7
                    with open('HPdata_test.json', "w") as g:
                        json.dump(hHP, g)
                    with open('file_HP', 'wb') as fh:
                        pickle.dump(hHP, fh)
                else:
                    print("You do not have any Wolf's meat\n--------------------------")

            if healChoise == 4:
                if "Wolf's heart" in inventory:
                    inventory.remove("Wolf's heart")
                    with open('inventorydata.json', 'w') as i:
                        json.dump(inventory, i)

                    with open('file_wolfInventory', 'wb') as fi:
                        pickle.dump(inventory, fi)
                    print("You used a Wolf's heart")
                    print("Your HP now is:", hHP + 10,"\n--------------------------")
                    hHP = hHP + 10

                    with open('HPdata_test.json', "w") as g:
                        json.dump(hHP, g)
                    with open('file_HP', 'wb') as fh:
                        pickle.dump(hHP, fh)
                else:
                    print("You do not have any Wolf's heart\n--------------------------")
        
# Blanace
    if string == 2:
        if coin < 0:
            print("It is impossible to have negative amount of money")
        else:
            print("Your balance:",coin,"FL\n--------------------------")


# Shop
    merchant = "Merchant"
    merchant_phrase1 = "Good day, adventurer"
    merchant_phrase2 = "What a lovely day!"
    merchant_phrase3 = "Are you looking for something?"
    merchant_phrase4 = "Welcome in Kabot shop"
    merchant_phrase5 = "I would like to see you are buying something"
    merchant_phrase_enter = [merchant_phrase1, merchant_phrase2, merchant_phrase3, merchant_phrase4, merchant_phrase5]
    merchant_phrase6 = "Sorry but you do not have enough FL"
    merchant_phrase7 = "Hey, I will not sell it for you for free!"
    merchant_phrase8 = "Mm, it is not on the house"
    merchant_phrase9 = "Money! Where is money?"
    merchant_phrase_buying = [merchant_phrase6, merchant_phrase7, merchant_phrase8, merchant_phrase9]

    merchant_phrase_in_enter = random.choices(merchant_phrase_enter)
    merchant_phrase_in_buying = random.choices(merchant_phrase_buying)

    shop = 'Y'

    
    if string == 3:
        print("You entered the shop\n--------------------------")

        while shop == 'Y':
            print(merchant,merchant_phrase_in_enter,"\n--------------------------")
            def sale(product,price,count,place):
                print("Product:",product,"; Price:",price,"FL; Count:",count,"| Type",place,"to buy this item")
            sale(product = "Jelly", price = 4, count = 5, place = 1)
            sale(product = "Pink jelly", price = 8, count = 2, place = 2)
            sale(product = "Wolf's meat", price = 10, count = 4, place = 3)
            sale(product = "Wolf's heart", price = 20, count = 1, place = 4)
            print("Type 0 to exit the shop")
            print("--------------------------")

            

            buying = int(input())
            if buying == 1:
                price1 = 4
                if coin < price1:
                    print(merchant,merchant_phrase_in_buying,"\n--------------------------")
                else:
                    print("You bought 'Jelly'\n--------------------------")

                    merchantInventory.remove("Jelly")
                    with open('merchantInvdata.json', 'w') as i:
                        json.dump(merchantInventory, i)
                    with open('file_merchantInventory', 'wb') as fi:
                        pickle.dump(merchantInventory, fi)

                    loot_from_slime1 = "Jelly"
                    inventory.append(loot_from_slime1)
                    with open('inventorydata.json', 'w') as i:
                        json.dump(inventory, i)
                    with open('file_wolfInventory', 'wb') as fi:
                        pickle.dump(inventory, fi)
                    
                    

                
                
                coin = coin - price1
                with open('coindata.json', 'w') as i:
                    json.dump(coin, i)
                shop = input('Stay in the shop? (y/n)').upper().strip()
                with open('file_coin', 'wb') as fi:
                    pickle.dump(coin, fi)

            if buying == 2:
                price2 = 8
                if coin < price2:
                    print(merchant,merchant_phrase_in_buying,"\n--------------------------")
                else:
                    print("You bought 'Pink jelly'\n--------------------------")
                    loot_from_slime2 = "Pink jelly"
                    inventory.append(loot_from_slime2)
                    with open('inventorydata.json', 'w') as i:
                        json.dump(inventory, i)
                    with open('file_wolfInventory', 'wb') as fi:
                        pickle.dump(inventory, fi)

                
                coin = coin - price2
                with open('coindata.json', 'w') as i:
                    json.dump(coin, i)
                shop = input('Stay in the shop? (y/n)').upper().strip()
                with open('file_coin', 'wb') as fi:
                    pickle.dump(coin, fi)

            if buying == 3:
                price3 = 10
                if coin < price3:
                    print(merchant,merchant_phrase_in_buying,"\n--------------------------")
                else:
                    print("You bought 'Wolf's meat'\n--------------------------")
                    loot_from_wolf1 = "Wolf's meat"
                    inventory.append(loot_from_wolf1)
                    with open('inventorydata.json', 'w') as i:
                        json.dump(inventory, i)
                    with open('file_wolfInventory', 'wb') as fi:
                        pickle.dump(inventory, fi)
                
                
                coin = coin - price3
                with open('coindata.json', 'w') as i:
                    json.dump(coin, i)
                shop = input('Stay in the shop? (y/n)').upper().strip()
                with open('file_coin', 'wb') as fi:
                    pickle.dump(coin, fi)

            if buying == 4:
                price4 = 20
                if coin < price4:
                    print(merchant,merchant_phrase_in_buying,"\n--------------------------")
                else:
                    print("You bought 'Wolf's heart'\n--------------------------")
                    loot_from_wolf2 = "Wolf's heart"
                    inventory.append(loot_from_wolf2)
                    with open('inventorydata.json', 'w') as i:
                        json.dump(inventory, i)
                    with open('file_wolfInventory', 'wb') as fi:
                        pickle.dump(inventory, fi)
                    
                    coin = coin - price4
                    with open('coindata.json', 'w') as i:
                        json.dump(coin, i)
                    shop = input('Stay in the shop? (y/n)').upper().strip()
                    with open('file_coin', 'wb') as fi:
                        pickle.dump(coin, fi)

            elif buying == 0:
                print('Exiting the shop\n--------------------------')
                shop = 'exit'

        



# Enemies


    prbty = random.randrange(1, 100)
    enemy_prbty = random.randrange(1, 3)
    loot_prbty = random.randrange(1,100)
    coin_prbty_from_slime = random.randrange(1,5)
    coin_prbty_from_wolf = random.randrange(4,15)

    #escape = random.randrange(1, 101)

    if string == 4:
        if prbty >= 71: 

            print("You found an enemy")
            if enemy_prbty == 1:
                print("It is slime")
                print(enemyst[0], slimeHP)
                print(enemyst[1], slimeATK)
                print("")
                print("What will you do?\nAttack: type 1") #\nEscape: type 2
                choise = int(input())
                if choise == 1:

                    #ATKhero = slice(1,2)
                    #print(lvlst[ATKhero])
                    #HPenemy = slice(0,1)
                    #print(slimelvl[HPenemy])
                    SlimeHP_after_bttl = slimeHP - hATK
                    print("Slime's HP:",SlimeHP_after_bttl)
                    if SlimeHP_after_bttl <= 0:
                        print("Slime is dead")

                        if loot_prbty <= 100:

                            loot_from_slime1 = "Jelly"
                            print("You found an",loot_from_slime1)
                            inventory.append(loot_from_slime1)
                            with open('inventorydata.json', 'w') as i:
                                json.dump(inventory, i)

                            with open('file_slimeInventory', 'wb') as fi:
                                pickle.dump(inventory, fi)
                        if loot_prbty <= 20:

                            loot_from_slime2 = "Pink jelly"
                            print("You found an",loot_from_slime2)
                            inventory.append(loot_from_slime2)
                            with open('inventorydata.json', 'w') as i:
                                json.dump(inventory, i)
                            with open('file_wolfInventory', 'wb') as fi:
                                pickle.dump(inventory, fi)

                        #if coin_prbty <= 50:
                        #    print()
                        coins = coin_prbty_from_slime
                        print("You get:",coins,"FL")
                        coin = coin + coins
                        with open('coindata.json', 'w') as i:
                            json.dump(coin, i)
                        with open('file_coin', 'wb') as fi:
                            pickle.dump(coin, fi)


                            



                        exp_from_slime = 2

                        exp.append(exp_from_slime)
                        print("You have",sum(exp),"exp\n--------------------------")
                        with open('expdata.json', 'w') as f:
                            json.dump(exp, f)
                        game = input('Continue the game? (y/n)').upper().strip()
                        with open('file_exp', 'wb') as fw:
                            pickle.dump(exp, fw)
                        print(nmst[0], hHP)
                        print(nmst[1], hATK)
                        print(nmst[2], hACC)
                        print(nmst[3], sum(exp),"\n--------------------------")




                    else:
                        print("Slime's HP: ",SlimeHP_after_bttl)
                        print("Slime is attacking\n--------------------------")
                #elif choise == 2:
                #    if escape >= 5:
                #        print("You have escaped\n--------------------------")
            elif enemy_prbty == 2:


                    print("It is wolf")
                    print(enemyst[0], wolfHP)
                    print(enemyst[1], wolfATK)
                    print("")
                    print("What will you do?\nAttack: type 1") #\nEscape: type 2
                    choise = int(input())
                    if choise == 1:

                        #ATKhero = slice(1,2)
                        #print(lvlst[ATKhero])
                        #HPenemy = slice(0,1)
                        #print(wolflvl[HPenemy])
                        WolfHP_after_bttl = wolfHP - hATK
                        print("Wolf's HP:", WolfHP_after_bttl)
                        if WolfHP_after_bttl <= 0:
                            print("Wolf is dead")
                            if loot_prbty <= 100:

                                loot_from_wolf1 = "Wolf's meat"
                                print("You found an",loot_from_wolf1)
                                inventory.append(loot_from_wolf1)
                                with open('inventorydata.json', 'w') as i:
                                    json.dump(inventory, i)

                                with open('file_wolfInventory', 'wb') as fi:
                                    pickle.dump(inventory, fi)
                            if loot_prbty <= 15:

                                loot_from_wolf2 = "Wolf's heart"
                                print("You found an",loot_from_wolf2)
                                inventory.append(loot_from_wolf2)
                                with open('inventorydata.json', 'w') as i:
                                    json.dump(inventory, i)
                                with open('file_wolfInventory', 'wb') as fi:
                                    pickle.dump(inventory, fi)

                            coins = coin_prbty_from_wolf
                            print("You get:",coins,"FL")
                            coin = coin + coins
                            with open('coindata.json', 'w') as i:
                                json.dump(coin, i)
                            with open('file_coin', 'wb') as fi:
                                pickle.dump(coin, fi)

                            exp_from_wolf = 6
                            exp.append(exp_from_wolf)
                            print("You have", sum(exp), "exp\n--------------------------")
                            with open('expdata.json', 'w') as f:
                                json.dump(exp, f)


                            game = input('Continue the game? (y/n)').upper().strip()
                            with open('file_exp', 'wb') as fw:
                                pickle.dump(exp, fw)

                            print(nmst[0], hHP)
                            print(nmst[1], hATK)
                            print(nmst[2], hACC)
                            print(nmst[3], sum(exp),"\n--------------------------")


                        elif WolfHP_after_bttl > 0:
                            #print("Wolf's HP: ", WolfHP_after_bttl)
                            print("Wolf is attacking")
                            hHP = hHP - wolfATK
                            print("Your HP:", hHP,"\n--------------------------")

                            with open('HPdata_test.json',"w") as g:
                                json.dump(hHP, g)
                            with open('file_HP', 'wb') as fh:
                                pickle.dump(hHP, fh)
                            if hHP > 0:
                                print("What will you do?\nAttack: type 1") #\nEscape: type 2
                                choise2 = int(input())


                                if choise2 == 1:
                                    WolfHP_after_bttl = WolfHP_after_bttl - hATK
                                    print("Wolf's HP:",WolfHP_after_bttl)
                                    if WolfHP_after_bttl <= 0:
                                        print("Wolf is dead\n--------------------------")
                                        if loot_prbty <= 100:

                                            loot_from_wolf1 = "Wolf's meat"
                                            print("You found an",loot_from_wolf1)
                                            inventory.append(loot_from_wolf1)
                                            with open('inventorydata.json', 'w') as i:
                                                json.dump(inventory, i)
                                            with open('file_wolfInventory', 'wb') as fi:
                                                pickle.dump(inventory, fi)
                                        if loot_prbty <= 15:

                                            loot_from_wolf2 = "Wolf's heart"
                                            print("You found an",loot_from_wolf2)
                                            inventory.append(loot_from_wolf2)
                                            with open('inventorydata.json', 'w') as i:
                                                json.dump(inventory, i)
                                            with open('file_wolfInventory', 'wb') as fi:
                                                pickle.dump(inventory, fi)

                                        coins = coin_prbty_from_wolf
                                        print("You get:",coins,"FL")
                                        coin = coin + coins
                                        with open('coindata.json', 'w') as i:
                                            json.dump(coin, i)
                                        with open('file_coin', 'wb') as fi:
                                            pickle.dump(coin, fi)

                                        exp_from_wolf = 6

                                        exp.append(exp_from_wolf)
                                        print("You have", sum(exp), "exp\n--------------------------")
                                        with open('expdata.json', 'w') as f:
                                            json.dump(exp, f)
                                        game = input('Continue the game? (y/n)').upper().strip()

                                        with open('file_exp', 'wb') as fw:
                                            pickle.dump(exp, fw)
                                        print(nmst[0], hHP)
                                        print(nmst[1], hATK)
                                        print(nmst[2], hACC)
                                        print(nmst[3], sum(exp),"\n--------------------------")


                                    elif WolfHP_after_bttl > 0:
                                        print("Wolf's HP: ", WolfHP_after_bttl)
                                        print("Wolf is attacking")
                                        h = hHP - wolfATK
                                        print("Your HP:", hHP)
                                        with open('HPdata_test.json', "w") as g:
                                            json.dump(hHP, g)
                                        with open('file_hp', 'wb') as fh:
                                            pickle.dump(hHP, fh)
                                        # elif choise == 2 CAN BE A CODE 'A1'
                            elif hHP <= 0:
                                print("You died")
# Restoring HP after death                               
                                hHP = 30
                                with open('HPdata_test.json', 'w') as h:
                                    json.dump(hHP, h)
                                with open('file_hp', 'wb') as fh:
                                    pickle.dump(hHP, fh)                         
# Clearing an inventory after death
                                inventorylist = [inventory]
                                with open('inventorydata.json', 'w') as i:
                                    json.dump(inventorylist, i)

                                with open('inventorydata.json') as Inventory_data:
                                    INVENTORYData = json.load(Inventory_data)
                                    INVENTORYData.remove(inventory)

                                with open('inventorydata.json', 'w') as qi:
                                    json.dump(INVENTORYData, qi)
                                inv = open('inventorydata.json')
                                Inv0 = json.load(inv)
                                inventory = [0]
                                #print(Inv0)                                                                         
# Dropping money after death4
                                coin = 0
                                with open('coindata.json', 'w') as c:
                                    json.dump(coin, c)

                                with open('coindata.json') as coin_data:
                                    COINdata = json.load(coin_data)
                                    COINdata = 0
# Restoring EXP
                                explist = [exp]
                                with open('expdata.json', 'w') as eXp:
                                    json.dump(explist, eXp)

                                with open('expdata.json') as EXP_data:
                                    EXPData = json.load(EXP_data)
                                    EXPData.remove(exp)

                                with open('expdata.json', 'w') as exP:
                                    json.dump(EXPData, exP)
                                eXp = open('expdata.json')
                                EXP0 = json.load(eXp)
                                exp = [0]
                                with open('expdata.json', 'w') as h:
                                    json.dump(exp, h)
                                game = input('Restart the game? (y/n)').upper().strip()
                                with open('file_exp', 'wb') as fh:
                                    pickle.dump(exp, fh)
                                print(nmst[0], hHP)
                                print(nmst[1], hATK)
                                print(nmst[2], hACC)
                                print(nmst[3], sum(exp), "\n--------------------------")
                


        else:

            print("You did not find anyone")

    
    
    
    if string == 0:
        print("Exiting...")
        game = 'n'
    

    
















'''

----------A1----------

                    elif choise == 2:
                        if escape >=90:
                            print("You have escaped\n--------------------------")




                        else:
                            print("Enemy's stats")
                            print(enemyst[0], wolfHP)
                            print(enemyst[1], wolfATK)
                            print("")
                            print("What will you do?\nAttack: type 1\nEscape: type 2")
                            choise = int(input())
                            if choise == 1:

                                # ATKhero = slice(1,2)
                                # print(lvlst[ATKhero])
                                # HPenemy = slice(0,1)
                                # print(wolflvl[HPenemy])
                                WolfHP_after_bttl = wolfHP - hATK
                                print("Wolf's HP:", WolfHP_after_bttl)
                                if WolfHP_after_bttl <= 0:
                                    print("Wolf is dead")
                                elif WolfHP_after_bttl > 0:
                                    # print("Wolf's HP: ", WolfHP_after_bttl)
                                    print("Wolf is attacking")
                                    h_after_bttl = hHP - wolfATK
                                    print("Your HP:", h_after_bttl, "\n--------------------------")
                                    if h_after_bttl > 0:
                                        print("What will you do?\nAttack: type 1\nEscape: type 2")
                                        choise2 = int(input())

                                        if choise2 == 1:
                                            WolfHP_after_bttl = WolfHP_after_bttl - hATK
                                            print("Wolf's HP:", WolfHP_after_bttl)
                                            if WolfHP_after_bttl <= 0:
                                                print("Wolf is dead\n--------------------------")
                                            elif WolfHP_after_bttl > 0:
                                                print("Wolf's HP: ", WolfHP_after_bttl)
                                                print("Wolf is attacking")
                                                h_after_bttl = hHP - wolfATK
                                                print("Your HP:", h_after_bttl)
'''