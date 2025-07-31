
class Computer:
    def __init__(self, name, cpu, ram, storage):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def computer_details(self):
        print(f"Computer name: {self.name}")
        print(f"Computer cpu: {self.cpu}")
        print(f"Computer ram: {self.ram}gb")
        print(f"Computer storage: {self.storage}gb")

    def start(self):
        print(f"{self.name} is starting..")


dell = Computer("Dell", "i5 10thgen", 8, 256)
hp = Computer("Hp", "i7 12thgen", 16, 512)

dell.computer_details()
hp.computer_details()


hp.start()
dell.start()
