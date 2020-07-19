class Token:
    def __init__(self, token):
        self.token = token

        self.head = Token.TokenHead(token[0:4])
        '''
        self.head.set_head(token[0])
        self.head.set_version(token[1])
        self.head.set_platform_id(token[2])
        self.head.set_length(token[3])
        '''
        self.tvl_rang = None
        self.tvl_cpuid = None
        self.tvl_product = None
        self.parse_tvls(token[4: len(token)])
        self.show_token()

    def parse_tvls(self, tvls):
        print("tvls len : " + str(len(tvls)))
        offset = 0
        self.tvl_rang = Token.TokenTLV(tvls[offset:offset + 2])
        offset += 2
        length = self.tvl_rang.get_len()
        self.tvl_rang.set_data(tvls[offset:offset + length])
        #print("offset = " + str(offset) + " length = " + str(length))
        offset += length

        self.tvl_product = Token.TokenTLV(tvls[offset:offset + 2])
        offset += 2
        length = self.tvl_product.get_len()
        self.tvl_product.set_data(tvls[offset:offset+length])
        #print("offset = " + str(offset) + " length = " + str(length))
        offset += length

        self.tvl_cpuid = Token.TokenTLV(tvls[offset:offset + 2])
        offset += 2
        length = self.tvl_cpuid.get_len()
        #print("cpuid len = " + str(length) + ", offset = " + str(offset))
        self.tvl_cpuid.set_data(tvls[offset:offset+length])
        #print("offset = " + str(offset) + " length = " + str(length))
        offset += length

    def show_token(self):
        self.head.show_head()
        self.tvl_rang.show_tvl()
        self.tvl_product.show_tvl()
        self.tvl_cpuid.show_tvl()

    class TokenHead:
        def __init__(self, head):
            self.head = head[0]
            self.version = head[1]
            self.platform_id = head[2]
            self.length = head[3]

        def show_head(self):
            print("head: " + hex(int(self.head)))
            print("version: " + hex(int(self.version)))
            print("platform_id: " + hex(int(self.platform_id)), end='')
            if self.platform_id == 1:
                print("(qcom)")
            elif self.platform_id == 2:
                print("(mtk)")
            elif self.platform_id == 3:
                print("(songguo)")
            print("data total length: " + str(int(self.length)))

    class TokenTLV:
        TYPE_RANG = 1
        TYPE_CPUID = 2
        TYPE_PRODUCE = 3

        def __init__(self, tvl_head):
            self.type = tvl_head[0]
            self.len = tvl_head[1]
            self.data = []

        def set_data(self, data):
            #print("data len: " + str(len(data)))
            self.data = data

        def get_len(self):
            return int(self.len)

        def show_tvl(self):
            if self.type == self.TYPE_RANG:
                print("type: " + hex(int(self.type)) + "(TYPE_RANG)")
            if self.type == self.TYPE_CPUID:
                print("type: " + hex(int(self.type)) + "(TYPE_CPUID)")
            if self.type == self.TYPE_PRODUCE:
                print("type: " + hex(int(self.type)) + "(TYPE_PRODUCE)")
            print("len: " + str((int(self.len))))
            if self.type == self.TYPE_RANG:
                print("rang data is : ", end='')
                for i in self.data:
                    print(i, end=' ')
                print()

            if self.type == self.TYPE_CPUID:
                print("cpuid: ", end='')
                id = 0
                for i in range(len(self.data)):
                    id = self.data[i] | (id << 8)
                print(hex(int(id)))

            if self.type == self.TYPE_PRODUCE:
                print("product: ", end='')
                for i in self.data:
                    print(chr(int(i)), end='')
                print()
