import random

class Encrypting:

    def __init__(self):
        self.p = random.randint(100,1000) # הפרמטר p חייב להיות מספר ראשוני גדול
        while not self.is_Prime(self.p):
            self.p = random.randint(100, 1000)


    def private_key(self, conn):
        # אלו המפתחות הציבוריים - המפתחות שכל הצדדים יודעים ומסכימים עליהם
        conn.send(str(self.p).encode()) # שולח את p לשרת
        g = int(conn.recv(2048).decode()) # מקבל את g משרת

        a = random.randint(1,10) # מפתח פרטי של הלקוח!!!! לא שולחים אותו באינטרנט

        A = (g ** a) % self.p
        conn.send(str(A).encode())
        B = int(conn.recv(2048).decode())

        K = (B ** a) % self.p
        return K

    def is_Prime(self, num):
        for i in range(2,num//2):
            if num % i == 0:
                return False
        return True