import mysql.connector
import datetime


class HotelManager:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Athulya@30",
            database="hotel_db"
        )

        print("Connected Successfully...")

    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()

            query = "SELECT * FROM booking WHERE id = %s"
            values = (id,)

            self.cursor.execute(query, values)
            record = self.cursor.fetchone()

            return record

        except Exception as e:
            print(e)


    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()

            query = """
            INSERT INTO booking
            (customer_name, phone, room_number, room_type,
            check_in, check_out, total_amount)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            values = [
                kwargs["customer_name"],
                kwargs["phone"],
                kwargs["room_number"],
                kwargs["room_type"],
                kwargs["check_in"],
                kwargs["check_out"],
                kwargs["total_amount"]
            ]

            self.cursor.execute(query, values)
            self.connection.commit()

            print("Booking added successfully...")

        except Exception as e:
            print(e)


    def get(self):
        try:
            self.cursor = self.connection.cursor()

            query = "SELECT * FROM booking"

            self.cursor.execute(query)
            records = self.cursor.fetchall()

            return records

        except Exception as e:
            print(e)
            return []


    def retrieve(self, id=None):
        try:
            record = self.get_object(id)

            if record != None:
                print(record)
            else:
                print("Booking not found...")

        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            record = self.get_object(id)
            values = (id,)

            if record != None:

                query = "DELETE FROM booking WHERE id = %s"

                self.cursor.execute(query, values)
                self.connection.commit()

                print("Booking deleted successfully...")

            else:
                print("Booking not found...")

        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)

            if record != None:

                self.cursor = self.connection.cursor()

                allowed_columns = [
                    "customer_name",
                    "phone",
                    "room_number",
                    "room_type",
                    "check_in",
                    "check_out",
                    "total_amount"
                ]


                for k in kwargs.keys():
                    if k not in allowed_columns:
                        print("Invalid column name:", k)
                        return

                if not kwargs:
                    print("No values provided for update...")
                    return

                placeholder = ""

                for k in kwargs.keys():
                    placeholder += k + "=%s, "

                placeholder = placeholder.rstrip(", ")

                query = f"UPDATE booking SET {placeholder} WHERE id = %s"

                values = [v for v in kwargs.values()]
                values.append(id)

                self.cursor.execute(query, values)
                self.connection.commit()

                print("Booking updated successfully...")

            else:
                print("Booking not found..!")

        except Exception as e:
            print(e)


hotel_instance = HotelManager()



# hotel_instance.post(customer_name="Anu", phone="9876543210", room_number=101, room_type="Deluxe", check_in=datetime.date.today(), check_out=datetime.date(2026, 11, 5), total_amount=4500)
# hotel_instance.post(customer_name="Aishu", phone="9876543211", room_number=102, room_type="Single", check_in=datetime.date.today(), check_out=datetime.date(2026, 8, 9), total_amount=2000)
# hotel_instance.post(customer_name="Aisha", phone="9876543212", room_number=103, room_type="Single", check_in=datetime.date.today(), check_out=datetime.date(2026, 11, 9), total_amount=2000)

#print(hotel_instance.get())

#hotel_instance.retrieve(1)

hotel_instance.delete(2)

hotel_instance.put(1, total_amount=5000)

hotel_instance.retrieve(1)