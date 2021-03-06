from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
import sqlite3

# Makes sure that there is always is a database
def createDBIfNotExist():
    conn = sqlite3.connect('magicCards.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS cards(
        card_name TEXT,
        type_1 TEXT,
        type_2 TEXT,
        type_3 TEXT,
        type_4 TEXT,
        type_5 TEXT,
        type_6 TEXT,
        type_7 TEXT,
        mana_type_1 TEXT,
        mana_type_2 TEXT,
        mana_cost_2 TEXT,
        power_toughness TEXT,
        card_number TEXT
    )""")

    conn.commit()
    conn.close()

# Look through database when program starts
def querydb():
    global card
    conn = sqlite3.connect('magicCards.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM cards")
    card = c.fetchall()

    # Add data to screen
    for card in card:
        if int(str(card[0])) % 2 == 0:
            treeTable.insert(parent = '', index = 'end', iid = card[0], text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13]), tags = ('evenrow',))
        else:
            treeTable.insert(parent = '', index = 'end', iid = card[0], text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13]), tags = ('oddrow',))

    conn.commit()
    conn.close()

# Function to help with clearing entry boxes
def clearEntryBoxes():
    itemNumberEntry.delete(0, END)
    cardNameEntry.delete(0, END)
    typeEntry.delete(0, END)
    subTypeEntry.delete(0, END)
    manaType1Entry.delete(0, END)
    manaType2Entry.delete(0, END)
    manaCost2Entry.delete(0, END)
    powerToughnessEntry.delete(0, END)
    cardNumberEntry.delete(0, END)
    type3Entry.delete(0, END)
    type4Entry.delete(0, END)
    type5Entry.delete(0, END)
    type6Entry.delete(0, END)
    type7Entry.delete(0, END)

def cardnamePopup():
    global cardNameTopEntry, cardNameTop
    cardNameTop = Toplevel(magicSorter)
    cardNameTop.title("Look Up Card Name")

    cardNameTopFrame = LabelFrame(cardNameTop, text = "Card Name:")
    cardNameTopFrame.pack(padx = 10, pady = 10)

    cardNameTopEntry = Entry(cardNameTopFrame, font=("Helvetica", 18), border = 2)
    cardNameTopEntry.pack(padx = 10, pady = 10)

    cardNameTopButton = Button(cardNameTopFrame, text = "Search cards", command = cardNameDatabase)
    cardNameTopButton.pack(padx= 10, pady = 10)

def typePopup():
    global type1TopEntry, type1Top
    type1Top = Toplevel(magicSorter)
    type1Top.title("Look Up the Type")

    type1TopFrame = LabelFrame(type1Top, text = "Type :")
    type1TopFrame.pack(padx = 10, pady = 10)

    type1TopEntry = Entry(type1TopFrame, font=("Helvetica", 18), border = 2)
    type1TopEntry.pack(padx = 10, pady = 10)

    type1TopButton = Button(type1TopFrame, text = "Search cards", command = typeDatabase)
    type1TopButton.pack(padx= 10, pady = 10)

def manaTypePopup():
    global manaTypeTopEntry, manaTypeTop
    manaTypeTop = Toplevel(magicSorter)
    manaTypeTop.title("Look Up the Mana Type")

    manaTypeTopFrame = LabelFrame(manaTypeTop, text = "Mana Type:")
    manaTypeTopFrame.pack(padx = 10, pady = 10)

    manaTypeTopEntry = Entry(manaTypeTopFrame, font=("Helvetica", 18), border = 2)
    manaTypeTopEntry.pack(padx = 10, pady = 10)

    manaTypeButton = Button(manaTypeTopFrame, text = "Search cards", command = manaTypeDatabase)
    manaTypeButton.pack(padx= 10, pady = 10)

def manaCostPopup():
    global manaCostTopEntry, manaCostTop
    manaCostTop = Toplevel(magicSorter)
    manaCostTop.title("Look Up the Mana Cost")

    manaCostTopFrame = LabelFrame(manaCostTop, text = "Mana Cost:")
    manaCostTopFrame.pack(padx = 10, pady = 10)

    manaCostTopEntry = Entry(manaCostTopFrame, font=("Helvetica", 18), border = 2)
    manaCostTopEntry.pack(padx = 10, pady = 10)

    manaCostButton = Button(manaCostTopFrame, text = "Search cards", command = manaCostDatabase)
    manaCostButton.pack(padx= 10, pady = 10)

def powerToughnessPopup():
    global powerToughnessTopEntry, powerToughnessTop
    powerToughnessTop = Toplevel(magicSorter)
    powerToughnessTop.title("Look Up the Power/Toughness")

    powerToughnessTopFrame = LabelFrame(powerToughnessTop, text = "Power/Toughness:")
    powerToughnessTopFrame.pack(padx = 10, pady = 10)

    powerToughnessTopEntry = Entry(powerToughnessTopFrame, font=("Helvetica", 18), border = 2)
    powerToughnessTopEntry.pack(padx = 10, pady = 10)

    powerToughnessTopButton = Button(powerToughnessTopFrame, text = "Search cards", command = powerToughnessDatabase)
    powerToughnessTopButton.pack(padx= 10, pady = 10)

def cardNumberPopup():
    global cardNumberTopEntry, cardNumberTop
    cardNumberTop = Toplevel(magicSorter)
    cardNumberTop.title("Look Up Card Number")

    cardNumberTopFrame = LabelFrame(cardNumberTop, text = "Card Number:")
    cardNumberTopFrame.pack(padx = 10, pady = 10)

    cardNumberTopEntry = Entry(cardNumberTopFrame, font=("Helvetica", 18), border = 2)
    cardNumberTopEntry.pack(padx = 10, pady = 10)

    cardNumberTopButton = Button(cardNumberTopFrame, text = "Search cards", command = cardNumberDatabase)
    cardNumberTopButton.pack(padx= 10, pady = 10)

def cardNameDatabase():
    searchCard = cardNameTopEntry.get()
    cardNameTop.destroy()

    for card in treeTable.get_children():
        treeTable.delete(card)

    conn = sqlite3.connect('magicCards.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM cards WHERE card_name like ?", (searchCard,))

    card = c.fetchall()

    # Add data to screen
    for card in card:
        if int(str(card[0])) % 2 == 0:
            treeTable.insert(parent = '', index = 'end', iid = card[0], text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13]), tags = ('evenrow',))
        else:
            treeTable.insert(parent = '', index = 'end', iid = card[0], text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13]), tags = ('oddrow',))

    conn.commit()
    conn.close()

def typeDatabase():
    searchCard = type1TopEntry.get()
    type1Top.destroy()

    for card in treeTable.get_children():
        treeTable.delete(card)

    conn = sqlite3.connect('magicCards.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM cards WHERE type_1 like ? OR type_2 like ? OR type_3 like ? OR type_4 like ? OR type_5 like ? OR type_6 like ? OR type_7 like ?", (searchCard, searchCard, searchCard, searchCard, searchCard, searchCard, searchCard,))

    card = c.fetchall()

    # Add data to screen
    for card in card:
        if int(str(card[0])) % 2 == 0:
            treeTable.insert(parent = '', index = 'end', iid = card[0], text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13]), tags = ('evenrow',))
        else:
            treeTable.insert(parent = '', index = 'end', iid = card[0], text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13]), tags = ('oddrow',))

    conn.commit()
    conn.close()

def manaTypeDatabase():
    searchCard = manaTypeTopEntry.get()
    manaTypeTop.destroy()

    for card in treeTable.get_children():
        treeTable.delete(card)

    conn = sqlite3.connect('magicCards.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM cards WHERE mana_type_2 like ? OR mana_type_1 like ?", (searchCard, searchCard))
    

    card = c.fetchall()

    # Add data to screen
    for card in card:
        if int(str(card[0])) % 2 == 0:
            treeTable.insert(parent = '', index = 'end', iid = card[0], text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13]), tags = ('evenrow',))
        else:
            treeTable.insert(parent = '', index = 'end', iid = card[0], text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13]), tags = ('oddrow',))

    conn.commit()
    conn.close()

def manaCostDatabase():
    searchCard = manaCostTopEntry.get()
    manaCostTop.destroy()

    for card in treeTable.get_children():
        treeTable.delete(card)

    conn = sqlite3.connect('magicCards.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM cards WHERE mana_cost_2 like ?", (searchCard,))

    card = c.fetchall()

    # Add data to screen
    for card in card:
        if int(str(card[0])) % 2 == 0:
            treeTable.insert(parent = '', index = 'end', iid = card[0], text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13]), tags = ('evenrow',))
        else:
            treeTable.insert(parent = '', index = 'end', iid = card[0], text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13]), tags = ('oddrow',))

    conn.commit()
    conn.close()

def powerToughnessDatabase():
    searchCard = powerToughnessTopEntry.get()
    powerToughnessTop.destroy()

    for card in treeTable.get_children():
        treeTable.delete(card)

    conn = sqlite3.connect('magicCards.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM cards WHERE power_toughness like ?", (searchCard,))

    card = c.fetchall()

    # Add data to screen
    for card in card:
        if int(str(card[0])) % 2 == 0:
            treeTable.insert(parent = '', index = 'end', iid = card[0], text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13]), tags = ('evenrow',))
        else:
            treeTable.insert(parent = '', index = 'end', iid = card[0], text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13]), tags = ('oddrow',))

    conn.commit()
    conn.close()

def cardNumberDatabase():
    searchCard = cardNumberTopEntry.get()
    cardNumberTop.destroy()

    for card in treeTable.get_children():
        treeTable.delete(card)

    conn = sqlite3.connect('magicCards.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM cards WHERE card_number like ?", (searchCard,))

    card = c.fetchall()

    # Add data to screen
    for card in card:
        if int(str(card[0])) % 2 == 0:
            treeTable.insert(parent = '', index = 'end', iid = card[0], text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13]), tags = ('evenrow',))
        else:
            treeTable.insert(parent = '', index = 'end', iid = card[0], text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13]), tags = ('oddrow',))

    conn.commit()
    conn.close()

def reloadAfterSearch():
    treeTable.delete(*treeTable.get_children())

    querydb()

# Adding a new card
def addACard():
    conn = sqlite3.connect('magicCards.db')
    c = conn.cursor()

    cardName = cardNameEntry.get()
    type1 = typeEntry.get()
    cardNumber = cardNumberEntry.get()
    manaType1 = manaType1Entry.get()
    manaType2 = manaType2Entry.get()
    manaCost = manaCost2Entry.get()

    if cardName == '':
        messagebox.showerror("Magic Card Sorter", "Please fill out the 'card name' box!")

    elif type1 == '':
        messagebox.showerror("Magic Card Sorter", "Please fill out 'type 1' box!")

    elif cardNumber == '':
        messagebox.showerror("Magic Card Sorter", "Please fill out the 'card number' box!")

    elif manaType1 == '':
        messagebox.showerror("Magic Card Sorter", "Please fill out the 'mana type 1' box!")

    elif manaType2 == '':
        messagebox.showerror("Magic Card Sorter", "Please fill out the 'mana type 2' box!")

    elif manaCost == '':
        messagebox.showerror("Magic Card Sorter", "Please fill out the 'mana cost' box!")

    else:
        c.execute("INSERT INTO cards VALUES(:card_name, :type_1, :type_2, :type_3, :type_4, :type_5, :type_6, :type_7, :mana_type_1, :mana_type_2, :mana_cost_1, :power_toughness, :card_number )", {
            'card_name' : cardNameEntry.get(), 
            'type_1' : typeEntry.get(), 
            'type_2' : subTypeEntry.get(),
            'type_3' : type3Entry.get(),
            'type_4' : type4Entry.get(),
            'type_5' : type5Entry.get(),
            'type_6' : type6Entry.get(),
            'type_7' : type7Entry.get(), 
            'mana_type_1' : manaType1Entry.get(),
            'mana_type_2' : manaType2Entry.get(), 
            'mana_cost_1' : manaCost2Entry.get(), 
            'power_toughness' : powerToughnessEntry.get(), 
            'card_number' : cardNumberEntry.get()
        })

    conn.commit()
    conn.close()

    clearEntryBoxes()

    treeTable.delete(*treeTable.get_children())

    querydb()

# Selecting a card
def selectACard(e):
    clearEntryBoxes()

    selected = treeTable.focus()

    values = treeTable.item(selected, 'values')

    itemNumberEntry.insert(0, values[0])
    cardNameEntry.insert(0, values[1])
    typeEntry.insert(0, values[2])
    subTypeEntry.insert(0, values[3])
    manaType1Entry.insert(0, values[9])
    manaType2Entry.insert(0, values[10])
    manaCost2Entry.insert(0, values[11])
    powerToughnessEntry.insert(0, values[12])
    cardNumberEntry.insert(0, values[13])
    type3Entry.insert(0, values[4])
    type4Entry.insert(0, values[5])
    type5Entry.insert(0, values[6])
    type6Entry.insert(0, values[7])
    type7Entry.insert(0, values[8])

# Updating card info
def updateACard():

    cardName = cardNameEntry.get()
    type1 = typeEntry.get()
    cardNumber = cardNumberEntry.get()
    manaType1 = manaType1Entry.get()
    manaType2 = manaType2Entry.get()
    manaCost = manaCost2Entry.get()

    if cardName == '':
        messagebox.showerror("Magic Card Sorter", "Please fill out the 'card name' box!")

    elif type1 == '':
        messagebox.showerror("Magic Card Sorter", "Please fill out 'type 1' box!")

    elif cardNumber == '':
        messagebox.showerror("Magic Card Sorter", "Please fill out the 'card number' box!")

    elif manaType1 == '':
        messagebox.showerror("Magic Card Sorter", "Please fill out the 'mana type 1' box!")

    elif manaType2 == '':
        messagebox.showerror("Magic Card Sorter", "Please fill out the 'mana type 2' box!")

    elif manaCost == '':
        messagebox.showerror("Magic Card Sorter", "Please fill out the 'mana cost' box!")

    else:
  
        selected = treeTable.focus()
        treeTable.item(selected, text = "", values = (
            itemNumberEntry.get(), 
            cardNameEntry.get(), 
            typeEntry.get(), 
            subTypeEntry.get(),
            type3Entry.get(),
            type4Entry.get(),
            type5Entry.get(),
            type6Entry.get(),
            type7Entry.get(), 
            manaType1Entry.get(),
            manaType2Entry.get(), 
            manaCost2Entry.get(), 
            powerToughnessEntry.get(), 
            cardNumberEntry.get()
            ))
    
        conn = sqlite3.connect('magicCards.db')
        c = conn.cursor()
    
        c.execute("""UPDATE cards SET
            card_name = :card_name,
            type_1 = :type_1,
            type_2 = :type_2,
            type_3 = :type_3,
            type_4 = :type_4,
            type_5 = :type_5,
            type_6 = :type_6,
            type_7 = :type_7,
            mana_type_1 = :mana_type_1,
            mana_type_2 = :mana_type_2,
            mana_cost_2 = :mana_cost_1,
            power_toughness = :power_toughness,
            card_number = :card_number 
    
            WHERE oid = :oid""", {
               'card_name' : cardNameEntry.get(), 
               'type_1' : typeEntry.get(), 
               'type_2' : subTypeEntry.get(),
               'type_3' : type3Entry.get(),
               'type_4' : type4Entry.get(),
               'type_5' : type5Entry.get(),
               'type_6' : type6Entry.get(),
               'type_7' : type7Entry.get(), 
               'mana_type_1' : manaType1Entry.get(),
               'mana_type_2' : manaType2Entry.get(), 
               'mana_cost_1' : manaCost2Entry.get(), 
               'power_toughness' : powerToughnessEntry.get(), 
               'card_number' : cardNumberEntry.get(),
               'oid' : card[0]
            })

        conn.commit()
        conn.close()

    clearEntryBoxes()

# Removing a card
def removeACard():
    x = treeTable.selection()[0]
    treeTable.delete(x)

    conn = sqlite3.connect('magicCards.db')
    c = conn.cursor()

    c.execute("DELETE FROM cards WHERE oid = " + itemNumberEntry.get())

    conn.commit()
    conn.close()

    messagebox.showinfo("Magic Card Sorter", "Your card has been deleted")

    clearEntryBoxes()

# Removing many cards
def removeMultipleCards():
    response = messagebox.askyesno("Magic Card Sorter", "Are you sure you want to delete the selected cards?")

    if response == 1:
        x = treeTable.selection()

        rowIDToDelete = []

        for card in x:
            rowIDToDelete.append(treeTable.item(card, 'values')[0])

        conn = sqlite3.connect('magicCards.db')
        c = conn.cursor()

        c.executemany("DELETE FROM cards WHERE oid = ?", [(n,) for n in rowIDToDelete])

        conn.commit()
        conn.close()

    for card in x:
        treeTable.delete(card)

    clearEntryBoxes()

# Removing everything
def removeCards():
    response = messagebox.askyesno("Magic Card Sorter", "Are you sure you want to delete every card?")

    if response == 1:
        conn = sqlite3.connect('magicCards.db')
        c = conn.cursor()

        c.execute("DROP TABLE cards")

        c.execute("""CREATE TABLE IF NOT EXISTS cards(
            card_name TEXT,
            type_1 TEXT,
            type_2 TEXT,
            type_3 TEXT,
            type_4 TEXT,
            type_5 TEXT,
            type_6 TEXT,
            type_7 TEXT,
            mana_type_1 TEXT,
            mana_type_2 TEXT,
            mana_cost_2 TEXT,
            power_toughness TEXT,
            card_number TEXT
        )""")

        conn.commit()
        conn.close()    

        clearEntryBoxes()

    for card in treeTable.get_children():
        treeTable.delete(card)

    querydb()

magicSorter = Tk()
magicSorter.title('Magic Card Sorter')

def evenRowColor():
    evenRowColor = colorchooser.askcolor()[1]

    if evenRowColor:
        # Create Striped Rows
        treeTable.tag_configure('evenrow', background = evenRowColor)

def oddRowColor():
    oddRowColor = colorchooser.askcolor()[1]

    if oddRowColor:
        # Create Striped Rows
        treeTable.tag_configure('oddrow', background = oddRowColor)

def highlightColor():
    highlightRowColor = colorchooser.askcolor()[1]
    
    if highlightRowColor:
        style.map('Treeview', 
            background = [('selected', highlightRowColor)])

def optionsIntruc():
    options = Tk()
    options.title("Options Instructions")

    instruc = LabelFrame(options)
    instruc.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

    optionsexplain = Label(instruc, text = "Using the 'Options Menu' you have three options \n EVEN ROW COLOR, ODD ROW COLOR and HIGHLIGHT COLOR \n ----- \n EVEN ROW COLOR is used to change the even row color \n ODD ROW COLOR is used to change the odd row color \n HIGHLIGHT COLOR is used to change of the row that is clicked on")
    optionsexplain.grid(row = 0, column = 0, padx = 10)

    close = Button(instruc, text = "Close", command = options.destroy, padx = 10, pady = 3)
    close.grid(row = 1, column = 0, padx = 10, pady = 10)

def searchInstruc():
    search = Tk()
    search.title("Search Instructions")

    instruc = LabelFrame(search)
    instruc.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

    searchexplain = Label(instruc, text = "Using the 'Search Menu' you have 6 things you can search \n CARD NAME, TYPES, MANA TYPES, MANA COST, POWER/TOUGHNESS \n and CARD NUMBER")
    searchexplain.grid(row = 0, column = 0, padx = 10)

    close = Button(instruc, text = "Close", command = search.destroy, padx = 10, pady = 3)
    close.grid(row = 1, column = 0, padx = 10, pady = 10)

def entriesInstruc():
    entries = Tk()
    entries.title("Entries Instructions")

    instruc = LabelFrame(entries)
    instruc.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

    entryexplain = Label(instruc, text = "Using the many different entry boxes on the bottom of the table.. you will \n use these to enter all the info from the cards \n ----- \n The required entries are \n Card Name, Type 1, Card Number, Mana Type 1 and 2, Power/Toughness \n and the Mana Cost")
    entryexplain.grid(row = 0, column = 0, padx = 10)

    close = Button(instruc, text = "Close", command = entries.destroy, padx = 10, pady = 3)
    close.grid(row = 1, column = 0, padx = 10, pady = 10)

def addACardInstruc():
    add = Tk()
    add.title("Add A Card Instructions")

    instruc = LabelFrame(add)
    instruc.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

    addCard = Button(instruc, text = "Add A Card")
    addCard.grid(row = 0, column = 0, padx = 10, pady = 10)

    explain = Label(instruc, text = "When adding a card there a few entry boxes that \n are required -refer back to the ENTRIES INSTRUCTIONS. Fill out \n the required fields and finally add your card")
    explain.grid(row = 1, column = 0, padx = 10)

    close = Button(instruc, text = "Close", command = add.destroy, padx = 10, pady = 3)
    close.grid(row = 2, column = 0, padx = 10, pady = 10)

def updateCardIntruc():
    update = Tk()
    update.title("Update Card Instructions")

    instruc = LabelFrame(update)
    instruc.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

    updateCard = Button(instruc, text = "Update Card")
    updateCard.grid(row = 0, column = 0, padx = 10, pady = 10)

    explain = Label(instruc, text = "When updating a card.. click on a row in the \n table.. then edit the the desired fields and press UPDATE \n CARD to finalize the changes")
    explain.grid(row = 1, column = 0, padx = 10)

    close = Button(instruc, text = "Close", command = update.destroy, padx = 10, pady = 3)
    close.grid(row = 2, column = 0, padx = 10, pady = 10)

def removeCardInsturc():
    removeOne = Tk()
    removeOne.title("Remove One Card Instructions")

    instruc = LabelFrame(removeOne)
    instruc.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

    removeCard = Button(instruc, text = "Remove Card")
    removeCard.grid(row = 0, column = 0, padx = 10, pady = 10)

    explain = Label(instruc, text = "To remove a card.. click on the row that has \n the card you want to delete.. then press REMOVE CARD")
    explain.grid(row = 1, column = 0, padx = 10)

    close = Button(instruc, text = "Close", command = removeOne.destroy, padx = 10, pady = 3)
    close.grid(row = 2, column = 0, padx = 10, pady = 10)

def removeMultipleCardsInstruc():
    removeMult = Tk()
    removeMult.title("Remove Multiple Cards Instructions")

    instruc = LabelFrame(removeMult)
    instruc.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

    removemultiCard = Button(instruc, text = "Remove Multiple Cards")
    removemultiCard.grid(row = 0, column = 0, padx = 10, pady = 10)

    explain = Label(instruc, text = "To remove multiple cards at once.. use ctrl + click to \n choose multiple at once")
    explain.grid(row = 1, column = 0, padx = 10)

    close = Button(instruc, text = "Close", command = removeMult.destroy, padx = 10, pady = 3)
    close.grid(row = 2, column = 0, padx = 10, pady = 10)

def removeAllCardsInstruc():
    removeAll = Tk()
    removeAll.title("Remove All Cards Instructions")

    instruc = LabelFrame(removeAll)
    instruc.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

    removeallCard = Button(instruc, text = "Remove All Cards")
    removeallCard.grid(row = 0, column = 0, padx = 10, pady = 10)

    explain = Label(instruc, text = "If you decide you want to start from the beginning \n and erase everything permanently use REMOVE ALL CARDS")
    explain.grid(row = 1, column = 0, padx = 10)

    close = Button(instruc, text = "Close", command = removeAll.destroy, padx = 10, pady = 3)
    close.grid(row = 2, column = 0, padx = 10, pady = 10)

def clearEntriesInstruc():
    clear = Tk()
    clear.title("Clear Entries Instructions")

    instruc = LabelFrame(clear)
    instruc.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

    removeallCard = Button(instruc, text = "Remove All Cards")
    removeallCard.grid(row = 0, column = 0, padx = 10, pady = 10)

    explain = Label(instruc, text = "If you dont want to manually clear the entries you \n can use this button to clear them all at once")
    explain.grid(row = 1, column = 0, padx = 10)

    close = Button(instruc, text = "Close", command = clear.destroy, padx = 10, pady = 3)
    close.grid(row = 2, column = 0, padx = 10, pady = 10)

def viewAllInstruc():
    viewAll = Tk()
    viewAll.title("View All Instructions")

    instruc = LabelFrame(viewAll)
    instruc.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

    finishsearch = Button(instruc, text = "Finish Search")
    finishsearch.grid(row = 0, column = 0, padx = 10, pady = 10)

    explain = Label(instruc, text = "After Searching use VIEW ALL the reload the table")
    explain.grid(row = 1, column = 0, padx = 10)

    close = Button(instruc, text = "Close", command = viewAll.destroy, padx = 10, pady = 3)
    close.grid(row = 2, column = 0, padx = 10, pady = 10)

# Create an option menu
itemMenu = Menu(magicSorter)
magicSorter.config(menu = itemMenu)

# Config option menu
optionMenu = Menu(itemMenu, tearoff = 0)
itemMenu.add_cascade(label = "Options", menu = optionMenu)

#Drop down option menu
optionMenu.add_command(label = "Even Row Color", command = evenRowColor)
optionMenu.add_command(label = "Odd Row Color", command = oddRowColor)
optionMenu.add_command(label = "Highlight Color", command = highlightColor)
optionMenu.add_separator()
optionMenu.add_command(label = "Exit", command = magicSorter.quit)

# Config search menu
searchMenu = Menu(itemMenu, tearoff = 0)
itemMenu.add_cascade(label = "Search", menu = searchMenu)

# Drop down search menu
searchMenu.add_command(label = "Card Name", command = cardnamePopup)
searchMenu.add_command(label = "Type", command = typePopup)
searchMenu.add_command(label = "Mana Type", command = manaTypePopup)
searchMenu.add_command(label = "Mana Cost", command = manaCostPopup)
searchMenu.add_command(label = "Power/Toughness", command = powerToughnessPopup)
searchMenu.add_command(label = "Card Number", command = cardNumberPopup)

# Config instructions menu
instrucMenu = Menu(itemMenu, tearoff = 0)
itemMenu.add_cascade(label = "Instructions", menu = instrucMenu)

# Drop down instructions menu
instrucMenu.add_command(label = "Options", command = optionsIntruc)
instrucMenu.add_command(label = "Search", command = searchInstruc)
instrucMenu.add_command(label = "Entries", command = entriesInstruc)
instrucMenu.add_command(label = "Add A Card", command = addACardInstruc)
instrucMenu.add_command(label = "Update Card", command = updateCardIntruc)
instrucMenu.add_command(label = "Remove Card", command = removeCardInsturc)
instrucMenu.add_command(label = "Remove Multiple Cards", command = removeMultipleCardsInstruc)
instrucMenu.add_command(label = "Remove All Cards", command = removeAllCardsInstruc)
instrucMenu.add_command(label = "Clear Entries", command = clearEntriesInstruc)
instrucMenu.add_command(label = "View All", command = viewAllInstruc)

# Styling
style = ttk.Style()

# Theme
style.theme_use('alt')

# Config Colors
style.configure("Treeview",
    background = "grey",
    foreground = "black",
    fieldbackground = "silver",
    rowheight = 25)

# Change selected color
style.map('Treeview',
    background = [('selected', '#A4A8A4')])

conn = sqlite3.connect('magicCards.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS cards(
    card_name TEXT,
    type_1 TEXT,
    type_2 TEXT,
    type_3 TEXT,
    type_4 TEXT,
    type_5 TEXT,
    type_6 TEXT,
    type_7 TEXT,
    mana_type_1 TEXT,
    mana_type_2 TEXT,
    mana_cost_2 TEXT,
    power_toughness TEXT,
    card_number TEXT
)""")

conn.commit()
conn.close()

# Create Treeview frame
treeFrame = Frame(magicSorter)
treeFrame.pack(padx = 10, pady = 10)

# Scrollbar
treeScrolly = Scrollbar(treeFrame)
treeScrolly.pack(side = RIGHT, fill = Y)

treeScrollx=Scrollbar(treeFrame, orient = 'horizontal')
treeScrollx.pack(side = BOTTOM, fill = 'x')

# Create Treeview
treeTable = ttk.Treeview(treeFrame, yscrollcommand = treeScrolly.set, xscrollcommand = treeScrollx.set, selectmode = "extended")
treeTable.pack()

# Scrollbar config
treeScrolly.config(command = treeTable.yview)
treeScrollx.config(command = treeTable.xview)

# Define columns
treeTable['columns'] = ("Item #", "Card Name", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 1", "Mana Type 2", "Mana Cost 2", "Power/Toughness", "Card Number")

# Format Columns
treeTable.column("#0", width = 0, stretch = NO)
treeTable.column("Item #", anchor = CENTER, width = 55, minwidth = 55)
treeTable.column("Card Name", anchor = CENTER, width = 150, stretch = YES)
treeTable.column("Type 1", anchor = CENTER, width = 100)
treeTable.column("Type 2", anchor = CENTER, width = 100)
treeTable.column("Type 3", anchor = CENTER, width = 100)
treeTable.column("Type 4", anchor = CENTER, width = 100)
treeTable.column("Type 5", anchor = CENTER, width = 100)
treeTable.column("Type 6", anchor = CENTER, width = 100)
treeTable.column("Type 7", anchor = CENTER, width = 100)
treeTable.column("Mana Type 1", anchor = CENTER, width = 100)
treeTable.column("Mana Type 2", anchor = CENTER, width = 100)
treeTable.column("Mana Cost 2", anchor = CENTER, width = 100)
treeTable.column("Power/Toughness", anchor = CENTER, width = 150)
treeTable.column("Card Number", anchor = CENTER, width = 110)

# Create Headings
treeTable.heading("#0", text = "", anchor = CENTER)
treeTable.heading("Item #", text = "Item #", anchor = CENTER)
treeTable.heading("Card Name", text = "Card Name", anchor = CENTER)
treeTable.heading("Type 1", text = "Type 1", anchor = CENTER)
treeTable.heading("Type 2", text = "Type 2", anchor = CENTER)
treeTable.heading("Type 3", text = "Type 3", anchor = CENTER)
treeTable.heading("Type 4", text = "Type 4", anchor = CENTER)
treeTable.heading("Type 5", text = "Type 5", anchor = CENTER)
treeTable.heading("Type 6", text = "Type 6", anchor = CENTER)
treeTable.heading("Type 7", text = "Type 7", anchor = CENTER)
treeTable.heading("Mana Type 1", text = "Mana Type 1", anchor = CENTER)
treeTable.heading("Mana Type 2", text = "Mana Type 2", anchor = CENTER)
treeTable.heading("Mana Cost 2", text = "Mana Cost", anchor = CENTER)
treeTable.heading("Power/Toughness", text = "Power/Toughness", anchor = CENTER)
treeTable.heading("Card Number", text = "Card Number", anchor = CENTER)

# Create Striped Rows
treeTable.tag_configure('oddrow', background = "lightblue")
treeTable.tag_configure('evenrow', background = "white")

# Add card data frame
cardDataFrame = LabelFrame(magicSorter, text = "Card Data:")
cardDataFrame.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

# Add card data label / entry boxes
itemNumberLabel = Label(cardDataFrame, text = "Item #:")
itemNumberLabel.grid(row = 0, column = 0, padx = 10, pady = 10)

itemNumberEntry = Entry(cardDataFrame, border = 2)
itemNumberEntry.grid(row = 0, column = 1, padx = 10, pady = 10)

cardNameLabel = Label(cardDataFrame, text = "Card Name:")
cardNameLabel.grid(row = 0, column = 2, padx = 10, pady = 10)

cardNameEntry = Entry(cardDataFrame, border = 2)
cardNameEntry.grid(row = 0, column = 3, padx = 10, pady = 10)

typeLabel = Label(cardDataFrame, text = "Type 1:")
typeLabel.grid(row = 0, column = 4, padx = 10, pady = 10)

typeEntry = Entry(cardDataFrame, border = 2)
typeEntry.grid(row = 0, column = 5, padx = 10, pady = 10)

subTypeLabel = Label(cardDataFrame, text = "Type 2:")
subTypeLabel.grid(row = 0, column = 6, padx = 10, pady = 10)

subTypeEntry = Entry(cardDataFrame, border = 2)
subTypeEntry.grid(row = 0, column = 7, padx = 10, pady = 10)

powerToughnessLabel = Label(cardDataFrame, text = "Power/Toughness:")
powerToughnessLabel.grid(row = 1, column = 0, padx = 10, pady = 10)

powerToughnessEntry = Entry(cardDataFrame, border = 2)
powerToughnessEntry.grid(row = 1, column = 1, padx = 10, pady = 10)

cardNumberLabel = Label(cardDataFrame, text = "Card Number:")
cardNumberLabel.grid(row = 1, column = 2, padx = 10, pady = 10)

cardNumberEntry = Entry(cardDataFrame, border = 2)
cardNumberEntry.grid(row = 1, column = 3, padx = 10, pady = 10)

# Add mana frame
manaDataFrame = LabelFrame(magicSorter, text = "Mana Types & Cost:")
manaDataFrame.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

# Add mana types & entry
manaType1Label = Label(manaDataFrame, text = "Mana Type 1:")
manaType1Label.grid(row = 0, column = 0, padx = 10, pady = 10)

manaType1Entry = Entry(manaDataFrame, border = 2)
manaType1Entry.grid(row = 0, column = 1, padx = 10, pady = 10)

manaType2Label = Label(manaDataFrame, text = "Mana Type 2:")
manaType2Label.grid(row = 0, column = 4, padx = 10, pady = 10)

manaType2Entry = Entry(manaDataFrame, border = 2)
manaType2Entry.grid(row = 0, column = 5, padx = 10, pady = 10)

manaCost2Label = Label(manaDataFrame, text = "Mana Cost:")
manaCost2Label.grid(row = 0, column = 6, padx = 10, pady = 10)

manaCost2Entry = Entry(manaDataFrame, border = 2)
manaCost2Entry.grid(row = 0, column = 7, padx = 10, pady = 10)

# Add extra type frame
typeDataFrame = LabelFrame(magicSorter, text = "Extra Types:")
typeDataFrame.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

# Add extra type label / entry boxes
type3Label = Label(typeDataFrame, text = "Type 3:")
type3Label.grid(row = 0, column = 0, padx = 10, pady = 10)

type3Entry = Entry(typeDataFrame, border = 2)
type3Entry.grid(row = 0, column = 1, padx = 10, pady = 10)

type4Label = Label(typeDataFrame, text = "Type 4:")
type4Label.grid(row = 0, column = 2, padx = 10, pady = 10)

type4Entry = Entry(typeDataFrame, border = 2)
type4Entry.grid(row = 0, column = 3, padx = 10, pady = 10)

type5Label = Label(typeDataFrame, text = "Type 5:")
type5Label.grid(row = 0, column = 4, padx = 10, pady = 10)

type5Entry = Entry(typeDataFrame, border = 2)
type5Entry.grid(row = 0, column = 5, padx = 10, pady = 10)

type6Label = Label(typeDataFrame, text = "Type 6:")
type6Label.grid(row = 0, column = 6, padx = 10, pady = 10)

type6Entry = Entry(typeDataFrame, border = 2)
type6Entry.grid(row = 0, column = 7, padx = 10, pady = 10)

type7Label = Label(typeDataFrame, text = "Type 7:")
type7Label.grid(row = 0, column = 8, padx = 10, pady = 10)

type7Entry = Entry(typeDataFrame, border = 2)
type7Entry.grid(row = 0, column = 9, padx = 10, pady = 10)

# Add button frame
commandDataFrame = LabelFrame(magicSorter, text = "Commands:")
commandDataFrame.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

# Add command buttons
addCard = Button(commandDataFrame, text = "Add A Card", command = addACard)
addCard.grid(row = 0, column = 0, padx = 10, pady = 10)

updateCard = Button(commandDataFrame, text = "Update Card", command = updateACard)
updateCard.grid(row = 0, column = 1, padx = 10, pady = 10)

removeCard = Button(commandDataFrame, text = "Remove Card", command = removeACard)
removeCard.grid(row = 0, column = 2, padx = 10, pady = 10)

removeManyCards = Button(commandDataFrame, text = "Remove Multiple Cards", command = removeMultipleCards)
removeManyCards.grid(row = 0, column = 3, padx = 10, pady = 10)

removeAllCards = Button(commandDataFrame, text = "Remove All Cards", command = removeCards)
removeAllCards.grid(row = 0, column = 4, padx = 10, pady = 10)

clearEntries = Button(commandDataFrame, text = "Clear Entries", command = clearEntryBoxes)
clearEntries.grid(row = 0, column = 5, padx = 10, pady = 10)

# Reload table after search
reloadTable = Button(commandDataFrame, text = "View All", command = reloadAfterSearch)
reloadTable.grid(row = 0, column = 6, padx = 10, pady = 10)

# Key binding
treeTable.bind("<ButtonRelease-1>", selectACard)

# Look through database when program starts
querydb()

# Create database if one does not exist
createDBIfNotExist()

# Closing window
magicSorter.mainloop()