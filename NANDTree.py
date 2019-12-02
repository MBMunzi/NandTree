class NANDTree:
    """ Instance a NandTree Object

        Attributes:
            levels (int): levels used to define tree levels.
            leaves (list): leaves are Data input to test.
    """
    def __init__(self, levels, leaves):
        self.leaves = leaves
        self.levels = levels
        self.validate_inputs()

    def validate_inputs(self):
        """ Used to test data inputs.

            Raises:
                Exception: Invalid input for NAND tree.
        """
        if int(self.levels) < 0:
            raise Exception("Invalid input for NAND tree. Levels, must be greater than zero.")
        if 2**(self.levels-1) != len(self.leaves):
            raise Exception("Invalid input for NAND tree. Leaves length must be multiple of two.")
        for value in self.leaves:
            if value not in (0, 1):
                raise Exception("Invalid input for NAND tree. The input must be boolean value, like zero or one.")
        print(self.leaves)

    def evaluate_simple(self, leaves=None):
        """ Used to evaluation Tree and obtain the root. About a pair of leaves.

            Args:
                leaves(list): Leaves ara data input

            Returns:
                new leaves: A sub-sequence leaves about other levels and call again function.
        """
        if leaves is None:
            leaves = self.leaves
        if len(leaves) == 1:
            return leaves[0]
        else:
            new_leaves = self.calculatenewleaves(leaves)
            return self.evaluate_simple(new_leaves)

    def calculatenewleaves(self, leaves):
        """ Used to calculate new leaves.

            Args:
                leaves(list): Leaves ara data input

            Returns:
                new leaves: Are a sub-sequence leaves about others levels tree.
        """
        leaves_pairs = [leaves[i:i+2] for i in range(0, len(leaves), 2)]
        new_leaves = []
        for pair in leaves_pairs:
            new_leaves.append(self.calculatenand(pair[0], pair[1]))
        print(new_leaves)
        return new_leaves

    def calculatenand(self, number1, number2):
        """ Used to calculate Logic Port Nand.

            Args:
                number1(int): Number 1 about boolean operation nand.
                number2(int): Number 2 about boolean operation nand.

            Returns:
                nand: Result, about boolean operation with Logic Port Nand.
        """
        nand = not(number1 and number2)
        nand = int(nand == True)
        return nand

    def evaluate_complex(self):
        """ Used to evaluation Tree and obtain the root. Start to left side Tree

            Returns:
                1: When boolean operation equal 0
                0: When Boolean operation equal 1
        """
        splited_leaves = [self.leaves[i:i+2]for i in range(2)]
        if self.calculatenewleaves(splited_leaves[0]) == 0:
            return 1
        else:
            if self.calculatenewleaves(splited_leaves[1]) == 0:
                return 1
            else:
                return 0

