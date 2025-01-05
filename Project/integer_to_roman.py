class Solution:
    def intToRoman(self, num: int) -> str:

        int_to_roman = ''
        list_of_parts = []
        romanIntegersMap = {
            1 : 'I',
            2 : 'II',
            3 : 'III',
            4 : 'IV',
            5 : 'V',
            6 : 'VI',
            7 : 'VII',
            8 : 'VIII',
            9 : 'IX',
            10 : 'X',
            20 : 'XX',
            30 : 'XXX',
            40 : 'XL',
            50 : 'L',
            60 : 'LX',
            70 : 'LXX',
            80 : 'LXXX',
            90 : 'XC',
            100 : 'C',
            200 : 'CC',
            300 : 'CCC',
            400 : 'CD',
            500 : 'D',
            600 : 'DC',
            700 : 'DCC',
            800 : 'DCCC',
            900 : 'CM',
            1000 : 'M',
            2000 : 'MM',
            3000 : 'MMM'
        }

        if num - 1000 >= 0:

            thousands = (num // 1000) * 1000
            hundreds = ((num - thousands) // 100) * 100
            tens = ((num - (thousands + hundreds)) // 10 ) * 10
            # for key, value in romanIntegersMap:
            #     if thousands == key:
            #         int_to_roman += key[value]
            # for key, value in romanIntegersMap:
            #     if hundreds == key:
            #         int_to_roman += key[value]
            # for key, value in romanIntegersMap:
            #     if tens == key:
            #         int_to_roman += key[value]

            list_of_parts += thousands, hundreds, tens
            for part in list_of_parts:
                int_to_roman += romanIntegersMap[part]
            int_to_roman += romanIntegersMap[( num % 10 )]

        elif num - 100 >= 0:
            hundreds = (num // 100) * 100
            tens = ((num - hundreds) // 10) * 10

            list_of_parts += hundreds, tens

            for part in list_of_parts:
                int_to_roman += romanIntegersMap[part]
            int_to_roman += romanIntegersMap[( num % 10 )]

        elif num - 10 >= 0:
            tens = (num // 10) * 10

            int_to_roman += romanIntegersMap[tens]
            int_to_roman += romanIntegersMap[( num % 10 )]

        return int_to_roman

number = 1994
print(Solution().intToRoman(number))