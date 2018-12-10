import tkinter as tk

class Clicker:
    def __init__(self, parent):
        self.parent = parent
        self.clicks = 0
        self.autoPower = 0
        self.clickPower = 1
        self.clickLabel = tk.Label(root, text = "Current clicks:\n" + str(self.clicks))
        self.clickLabel.pack()

        #Click
        self.clickButton = tk.Button(root, text = "Get clicks!", width=25, command = self.add)
        self.clickButton.pack()

        #UpgradePower
        self.upgradeButton = tk.Button(root, text = "Upgrade Click Power!" , width=25, command = self.buyPower)
        self.upgradeButton.pack()
        self.clickPowerLabel = tk.Label(root, text = "Current:" + str(self.clickPower))
        self.clickPowerLabel.pack()

        #UpgradeAuto
        self.upgradeAutoButton = tk.Button(root, text = "Upgrade Automatic Power!", width=25, command = self.buyautoPower)
        self.upgradeAutoButton.pack()
        self.autoPowerLabel = tk.Label(root, text = "Clicks per second:\n" + str(self.autoPower))
        self.autoPowerLabel.pack()

        #Quitting
        self.quitButton = tk.Button(root, text = "Stop", width=25, command = root.destroy)
        self.quitButton.pack()


        self.update()

    def add(self):
        self.clicks += self.clickPower
        self.clickLabel.config(text = "Current clicks:\n" + str(self.clicks))

    def buyPower(self):
        if self.clicks > 10:
            self.clickPower += 1
            self.clicks -= 10
            self.clickPowerLabel.config(text = "Current:" + str(self.clickPower))
            self.clickLabel.config(text = "Current clicks:\n" + str(self.clicks))

    def buyautoPower(self):
        if self.clicks > 100:
            self.autoPower += 1
            self.clicks -= 100
            self.autoPowerLabel.config(text = "Clicks per second:\n" + str(self.autoPower))
            self.clickLabel.config(text = "Current clicks:\n" + str(self.clicks))

    def update(self):
        per_second = self.autoPower
        additional = int(per_second)
        self.clicks += additional
        self.clickLabel.config(text='Current clicks:\n' + str(self.clicks))
        self.parent.after(1000, self.update)


root = tk.Tk()
clicker = Clicker(root)
root.mainloop()
