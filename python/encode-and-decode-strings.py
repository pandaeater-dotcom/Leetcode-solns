class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ""
        for string in strs:
            encoded_string += f"{len(string)}:{string}"
        return encoded_string

    

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strings = []
        def recursive_decode(s: str):
            dividerIndex = s.find(':')
            if dividerIndex == -1:
                return
            stringLength = int(s[:dividerIndex])
            stringStart = dividerIndex + 1
            stringEnd = stringStart + stringLength

            decoded_strings.append(s[stringStart:stringEnd])
            recursive_decode(s[stringEnd:])

        recursive_decode(s)
        return decoded_strings

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
