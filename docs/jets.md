# Simplicity Jets Reference

**Status:** Verified against Haskell source code  
**Last Updated:** 2024

---

## Table of Contents

- [Core Jets](#core-jets) 
- [Elements Jets](#elements-jets) 
- [Bitcoin Jets](#bitcoin-jets) 

---

## Type Notation Guide

### Basic Types
- `()` - Unit type (no value)
- `Bit` - Single bit (0 or 1)
- `WordN` - N-bit unsigned integer (Word8, Word16, Word32, Word64, Word128, Word256)
- `(A, B)` - Tuple/pair of types
- `Maybe A` - Optional value
- `Either A B` - One of two types

### Crypto Types
- `FE` - Field element (secp256k1)
- `Scalar` - Scalar value (curve order)
- `GEJ` - Jacobian point (X, Y, Z)
- `GE` - Affine point (x, y)
- `PubKey` - Public key (32 bytes)
- `Sig` - Signature (64 bytes)

### Transaction Types
- `ConfWord256` - Confidential (blinded) 256-bit value
- `ConfWord64` - Confidential (blinded) 64-bit value
- `Hash256` - SHA256 hash (32 bytes)

---

## Core Jets

### Arithmetic Operations

#### `Add(8/16/32/64)`

**Type:** `(WordN, WordN) -> (Bit, WordN)`

**Description:** Addition of two n-bit words returning carry bit and sum

#### `Decrement(8/16/32/64)`

**Type:** `WordN -> (Bit, WordN)`

**Description:** Decrement n-bit word by 1 returning borrow bit and result

#### `DivMod(8/16/32/64)`

**Type:** `(WordN, WordN) -> (WordN, WordN)`

**Description:** Division and modulo of two n-bit words returning quotient and remainder

#### `DivMod128_64`

**Type:** `(Word128, Word64) -> (Word64, Word64)`

**Description:** Divide 128-bit word by 64-bit word returning quotient and remainder

#### `Divide(8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Division of two n-bit words returning quotient

#### `Divides(8/16/32/64)`

**Type:** `(WordN, WordN) -> Bit`

**Description:** Check if first n-bit word divides the second

#### `FeAdd`

**Type:** `(FE, FE) -> FE`

**Description:** Add two secp256k1 field elements

#### `FeMultiply`

**Type:** `(FE, FE) -> FE`

**Description:** Multiply two secp256k1 field elements

#### `FeMultiplyBeta`

**Type:** `FE -> FE`

**Description:** Multiply secp256k1 field element by beta constant

#### `FeNegate`

**Type:** `FE -> FE`

**Description:** Negate secp256k1 field element

#### `FullAdd(8/16/32/64)`

**Type:** `(Bit, (WordN, WordN)) -> (Bit, WordN)`

**Description:** Full adder with carry input for n-bit words

#### `FullDecrement(8/16/32/64)`

**Type:** `(Bit, WordN) -> (Bit, WordN)`

**Description:** Decrement with borrow input for n-bit words

#### `FullIncrement(8/16/32/64)`

**Type:** `(Bit, WordN) -> (Bit, WordN)`

**Description:** Increment with carry input for n-bit words

#### `FullMultiply(8/16/32/64)`

**Type:** `((WordN, WordN), (WordN, WordN)) -> Word(2N)`

**Description:** Multiply two n-bit words with two carry words producing 2n-bit result

#### `FullSubtract(8/16/32/64)`

**Type:** `(Bit, (WordN, WordN)) -> (Bit, WordN)`

**Description:** Full subtractor with borrow input for n-bit words

#### `GeNegate`

**Type:** `GE -> GE`

**Description:** Negate affine elliptic curve point

#### `GejAdd`

**Type:** `(GEJ, GEJ) -> GEJ`

**Description:** Add two Jacobian elliptic curve points

#### `GejGeAdd`

**Type:** `(GEJ, GE) -> GEJ`

**Description:** Add Jacobian point to affine point

#### `GejGeAddEx`

**Type:** `(GEJ, GE) -> (FE, GEJ)`

**Description:** Add Jacobian point to affine point with extra output

#### `GejNegate`

**Type:** `GEJ -> GEJ`

**Description:** Negate Jacobian elliptic curve point

#### `Increment(8/16/32/64)`

**Type:** `WordN -> (Bit, WordN)`

**Description:** Increment n-bit word by 1 returning carry bit and result

#### `Max(8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Return maximum of two n-bit words

#### `Median(8/16/32/64)`

**Type:** `(WordN, (WordN, WordN)) -> WordN`

**Description:** Return median value of three n-bit words

#### `Min(8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Return minimum of two n-bit words

#### `Modulo(8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Compute modulo (remainder) of first n-bit word divided by second

#### `Multiply(8/16/32/64)`

**Type:** `(WordN, WordN) -> Word(2N)`

**Description:** Multiply two n-bit words producing 2n-bit result

#### `Negate(8/16/32/64)`

**Type:** `WordN -> (Bit, WordN)`

**Description:** Two's complement negation of n-bit word

#### `ScalarAdd`

**Type:** `(Scalar, Scalar) -> Scalar`

**Description:** Add two secp256k1 scalars

#### `ScalarMultiply`

**Type:** `(Scalar, Scalar) -> Scalar`

**Description:** Multiply two secp256k1 scalars

#### `ScalarMultiplyLambda`

**Type:** `Scalar -> Scalar`

**Description:** Multiply secp256k1 scalar by lambda constant

#### `ScalarNegate`

**Type:** `Scalar -> Scalar`

**Description:** Negate secp256k1 scalar

#### `Sha256Ctx8Add(1/2/4/8/16/32/64/128/256/512)`

**Type:** `(Ctx8, WordN) -> Ctx8`

**Description:** Add n-bit data to SHA256 context

#### `Sha256Ctx8AddBuffer511`

**Type:** `(Ctx8, Buffer511) -> Ctx8`

**Description:** Add buffer up to 511 bytes to SHA256 context

#### `Subtract(8/16/32/64)`

**Type:** `(WordN, WordN) -> (Bit, WordN)`

**Description:** Subtraction of two n-bit words returning borrow bit and difference

### Bitwise Logic

#### `And(1/8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Bitwise AND of two n-bit words

#### `Ch(1/8/16/32/64)`

**Type:** `(WordN, (WordN, WordN)) -> WordN`

**Description:** Bitwise choice: for each bit position, if bit in first word is 1 choose from second word, else choose from third word

#### `CheckSigVerify`

**Type:** `((PubKey, Word512), Sig) -> ()`

**Description:** Verify Schnorr signature and fail if invalid

#### `Complement(1/8/16/32/64)`

**Type:** `WordN -> WordN`

**Description:** Bitwise NOT (complement) of n-bit word

#### `Maj(1/8/16/32/64)`

**Type:** `(WordN, (WordN, WordN)) -> WordN`

**Description:** Majority function: returns bitwise majority of three n-bit words

#### `Or(1/8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Bitwise OR of two n-bit words

#### `Xor(1/8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Bitwise XOR of two n-bit words

#### `XorXor(1/8/16/32/64)`

**Type:** `(WordN, (WordN, WordN)) -> WordN`

**Description:** XOR of three n-bit words (a XOR b XOR c)

### Comparison & Testing

#### `All(8/16/32/64)`

**Type:** `WordN -> Bit`

**Description:** Test if all bits are set in n-bit word

#### `Eq(1/8/16/32/64/256)`

**Type:** `(WordN, WordN) -> Bit`

**Description:** Test equality of two n-bit words

#### `FeIsZero`

**Type:** `FE -> Bit`

**Description:** Test if secp256k1 field element is zero

#### `FullLeftShift16_(1/2/4/8)`

**Type:** `(Word16, WordK) -> (WordK, Word16)`

**Description:** Left shift 16-bit word by k bits returning shifted-out bits and result

#### `FullLeftShift32_(1/2/4/8/16)`

**Type:** `(Word32, WordK) -> (WordK, Word32)`

**Description:** Left shift 32-bit word by k bits returning shifted-out bits and result

#### `FullLeftShift64_(1/2/4/8/16/32)`

**Type:** `(Word64, WordK) -> (WordK, Word64)`

**Description:** Left shift 64-bit word by k bits returning shifted-out bits and result

#### `FullLeftShift8_(1/2/4)`

**Type:** `(Word8, WordK) -> (WordK, Word8)`

**Description:** Left shift 8-bit word by k bits returning shifted-out bits and result

#### `GejEquiv`

**Type:** `(GEJ, GEJ) -> Bit`

**Description:** Test equivalence of two Jacobian points

#### `GejGeEquiv`

**Type:** `(GEJ, GE) -> Bit`

**Description:** Test equivalence of Jacobian and affine points

#### `GejXEquiv`

**Type:** `(FE, GEJ) -> Bit`

**Description:** Test if Jacobian point has given x-coordinate

#### `IsOne(8/16/32/64)`

**Type:** `WordN -> Bit`

**Description:** Test if n-bit word is one

#### `IsZero(8/16/32/64)`

**Type:** `WordN -> Bit`

**Description:** Test if n-bit word is zero

#### `Le(8/16/32/64)`

**Type:** `(WordN, WordN) -> Bit`

**Description:** Test if first n-bit word is less than or equal to second

#### `LeftExtend16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Sign-extend 16-bit word to wider word by replicating the MSB on the left

#### `LeftExtend1_(8/16/32/64)`

**Type:** `Word1 -> WordN`

**Description:** Sign-extend 1-bit value to wider word by replicating the bit on the left

#### `LeftExtend32_64`

**Type:** `Word32 -> Word64`

**Description:** Sign-extend 32-bit word to 64-bit by replicating the MSB on the left

#### `LeftExtend8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Sign-extend 8-bit word to wider word by replicating the MSB on the left

#### `LeftPadHigh16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Pad 16-bit word to wider word with zeros on the right (high side)

#### `LeftPadHigh1_(8/16/32/64)`

**Type:** `Word1 -> WordN`

**Description:** Pad 1-bit value to wider word with zeros on the right (high side)

#### `LeftPadHigh32_64`

**Type:** `Word32 -> Word64`

**Description:** Pad 32-bit word to 64-bit with zeros on the right (high side)

#### `LeftPadHigh8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Pad 8-bit word to wider word with zeros on the right (high side)

#### `LeftPadLow16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Pad 16-bit word to wider word with zeros on the left (low side)

#### `LeftPadLow1_(8/16/32/64)`

**Type:** `Word1 -> WordN`

**Description:** Pad 1-bit value to wider word with zeros on the left (low side)

#### `LeftPadLow32_64`

**Type:** `Word32 -> Word64`

**Description:** Pad 32-bit word to 64-bit with zeros on the left (low side)

#### `LeftPadLow8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Pad 8-bit word to wider word with zeros on the left (low side)

#### `LeftRotate(8/16/32/64)`

**Type:** `(Word4/Word8, WordN) -> WordN`

**Description:** Left rotate (circular shift) n-bit word

#### `LeftShift(8/16/32/64)`

**Type:** `(Word4/Word8, WordN) -> WordN`

**Description:** Left shift n-bit word by specified amount

#### `LeftShiftWith(8/16/32/64)`

**Type:** `(Bit, (Word4/Word8, WordN)) -> WordN`

**Description:** Left shift n-bit word filling with specified bit

#### `Leftmost16_(1/2/4/8)`

**Type:** `Word16 -> WordK`

**Description:** Extract leftmost (most significant) k bits from 16-bit word

#### `Leftmost32_(1/2/4/8/16)`

**Type:** `Word32 -> WordK`

**Description:** Extract leftmost (most significant) k bits from 32-bit word

#### `Leftmost64_(1/2/4/8/16/32)`

**Type:** `Word64 -> WordK`

**Description:** Extract leftmost (most significant) k bits from 64-bit word

#### `Leftmost8_(1/2/4)`

**Type:** `Word8 -> WordK`

**Description:** Extract leftmost (most significant) k bits from 8-bit word

#### `Lt(8/16/32/64)`

**Type:** `(WordN, WordN) -> Bit`

**Description:** Test if first n-bit word is less than second

#### `ScalarIsZero`

**Type:** `Scalar -> Bit`

**Description:** Test if secp256k1 scalar is zero

#### `Some(1/8/16/32/64)`

**Type:** `WordN -> Bit`

**Description:** Test if any bit is set in n-bit word (returns true if word is non-zero)

### Shift & Rotate

#### `FullRightShift16_(1/2/4/8)`

**Type:** `(WordK, Word16) -> (Word16, WordK)`

**Description:** Right shift 16-bit word by k bits returning result and shifted-out bits

#### `FullRightShift32_(1/2/4/8/16)`

**Type:** `(WordK, Word32) -> (Word32, WordK)`

**Description:** Right shift 32-bit word by k bits returning result and shifted-out bits

#### `FullRightShift64_(1/2/4/8/16/32)`

**Type:** `(WordK, Word64) -> (Word64, WordK)`

**Description:** Right shift 64-bit word by k bits returning result and shifted-out bits

#### `FullRightShift8_(1/2/4)`

**Type:** `(WordK, Word8) -> (Word8, WordK)`

**Description:** Right shift 8-bit word by k bits returning result and shifted-out bits

#### `RightRotate(8/16/32/64)`

**Type:** `(Word4/Word8, WordN) -> WordN`

**Description:** Right rotate (circular shift) n-bit word

#### `RightShift(8/16/32/64)`

**Type:** `(Word4/Word8, WordN) -> WordN`

**Description:** Right shift n-bit word by specified amount

#### `RightShiftWith(8/16/32/64)`

**Type:** `(Bit, (Word4/Word8, WordN)) -> WordN`

**Description:** Right shift n-bit word filling with specified bit

### Bit Manipulation

#### `RightExtend16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Sign-extend 16-bit word to wider word by replicating the LSB on the right

#### `RightExtend32_64`

**Type:** `Word32 -> Word64`

**Description:** Sign-extend 32-bit word to 64-bit by replicating the LSB on the right

#### `RightExtend8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Sign-extend 8-bit word to wider word by replicating the LSB on the right

#### `RightPadHigh16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Pad 16-bit word to wider word with zeros on the left (high side)

#### `RightPadHigh1_(8/16/32/64)`

**Type:** `Word1 -> WordN`

**Description:** Pad 1-bit value to wider word with zeros on the left (high side)

#### `RightPadHigh32_64`

**Type:** `Word32 -> Word64`

**Description:** Pad 32-bit word to 64-bit with zeros on the left (high side)

#### `RightPadHigh8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Pad 8-bit word to wider word with zeros on the left (high side)

#### `RightPadLow16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Pad 16-bit word to wider word with zeros on the right (low side)

#### `RightPadLow1_(8/16/32/64)`

**Type:** `Word1 -> WordN`

**Description:** Pad 1-bit value to wider word with zeros on the right (low side)

#### `RightPadLow32_64`

**Type:** `Word32 -> Word64`

**Description:** Pad 32-bit word to 64-bit with zeros on the right (low side)

#### `RightPadLow8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Pad 8-bit word to wider word with zeros on the right (low side)

#### `Rightmost16_(1/2/4/8)`

**Type:** `Word16 -> WordK`

**Description:** Extract rightmost (least significant) k bits from 16-bit word

#### `Rightmost32_(1/2/4/8/16)`

**Type:** `Word32 -> WordK`

**Description:** Extract rightmost (least significant) k bits from 32-bit word

#### `Rightmost64_(1/2/4/8/16/32)`

**Type:** `Word64 -> WordK`

**Description:** Extract rightmost (least significant) k bits from 64-bit word

#### `Rightmost8_(1/2/4)`

**Type:** `Word8 -> WordK`

**Description:** Extract rightmost (least significant) k bits from 8-bit word

### Constants

#### `High(1/8/16/32/64)`

**Type:** `() -> WordN`

**Description:** Constant word with all bits set to 1

#### `Low(1/8/16/32/64)`

**Type:** `() -> WordN`

**Description:** Constant word with all bits set to 0

#### `One(8/16/32/64)`

**Type:** `() -> WordN`

**Description:** Constant word with value 1

### Secp256k1 Field Elements

#### `FeInvert`

**Type:** `FE -> FE`

**Description:** Compute multiplicative inverse of secp256k1 field element

#### `FeIsOdd`

**Type:** `FE -> Bit`

**Description:** Test if secp256k1 field element is odd

#### `FeNormalize`

**Type:** `FE -> FE`

**Description:** Normalize secp256k1 field element to canonical form

#### `FeSquare`

**Type:** `FE -> FE`

**Description:** Square secp256k1 field element

#### `FeSquareRoot`

**Type:** `FE -> Maybe FE`

**Description:** Compute square root of secp256k1 field element if it exists

### Secp256k1 Scalars

#### `ScalarInvert`

**Type:** `Scalar -> Scalar`

**Description:** Compute multiplicative inverse of secp256k1 scalar

#### `ScalarNormalize`

**Type:** `Scalar -> Scalar`

**Description:** Normalize secp256k1 scalar to canonical form

#### `ScalarSquare`

**Type:** `Scalar -> Scalar`

**Description:** Square secp256k1 scalar

### Secp256k1 Points

#### `GeIsOnCurve`

**Type:** `GE -> Bit`

**Description:** Test if affine point is on the secp256k1 curve

#### `GejDouble`

**Type:** `GEJ -> GEJ`

**Description:** Double Jacobian elliptic curve point

#### `GejInfinity`

**Type:** `() -> GEJ`

**Description:** Create point at infinity in Jacobian coordinates

#### `GejIsInfinity`

**Type:** `GEJ -> Bit`

**Description:** Test if Jacobian point is at infinity

#### `GejIsOnCurve`

**Type:** `GEJ -> Bit`

**Description:** Test if Jacobian point is on the curve

#### `GejNormalize`

**Type:** `GEJ -> Maybe GE`

**Description:** Normalize Jacobian point to affine coordinates

#### `GejRescale`

**Type:** `(GEJ, FE) -> GEJ`

**Description:** Rescale Jacobian point by field element

#### `GejYIsOdd`

**Type:** `GEJ -> Bit`

**Description:** Test if y-coordinate of Jacobian point is odd

#### `Generate`

**Type:** `Scalar -> GEJ`

**Description:** Generate secp256k1 public key from scalar (scalar multiplication by generator point)

### Elliptic Curve Operations

#### `Decompress`

**Type:** `Point -> Maybe GE`

**Description:** Decompress secp256k1 public key from x-coordinate

#### `HashToCurve`

**Type:** `Word256 -> GE`

**Description:** Hash arbitrary data to curve point

#### `LinearCombination1`

**Type:** `((Scalar, GEJ), Scalar) -> GEJ`

**Description:** Compute s1*P1 + s2*G where s1,s2 are scalars, P1 is a point, G is generator

#### `LinearVerify1`

**Type:** `(((Scalar, GE), Scalar), GE) -> ()`

**Description:** Verify that s1*P1 + s2*P2 = point at infinity (linear combination check)

#### `PointVerify1`

**Type:** `(((Scalar, Point), Scalar), Point) -> ()`

**Description:** Verify Schnorr signature equation using linear combination

#### `Scale`

**Type:** `(Scalar, GEJ) -> GEJ`

**Description:** Scalar multiplication of curve point

#### `Swu`

**Type:** `FE -> GE`

**Description:** Shallue-van de Woestijne encoding to curve point

### Signatures

#### `Bip0340Verify`

**Type:** `((PubKey, Word256), Sig) -> ()`

**Description:** Verify BIP-340 Schnorr signature

#### `Verify`

**Type:** `Bit -> ()`

**Description:** Assert that input bit is true (fail if false)

### SHA256 Hashing

#### `Sha256Block`

**Type:** `(Hash256, Block512) -> Hash256`

**Description:** Process single 512-bit block through SHA256 compression function

#### `Sha256Ctx8Finalize`

**Type:** `Ctx8 -> Hash256`

**Description:** Finalize SHA256 hash computation from context returning hash digest

#### `Sha256Ctx8Init`

**Type:** `() -> Ctx8`

**Description:** Initialize SHA256 context to initial state

#### `Sha256Iv`

**Type:** `() -> Hash256`

**Description:** Get SHA256 initial values

### Time Locks

#### `ParseLock`

**Type:** `Word32 -> Either Word32 Word32`

**Description:** Parse lock time from transaction data

#### `ParseSequence`

**Type:** `Word32 -> Maybe (Either Word16 Word16)`

**Description:** Parse sequence number from input data

### Taproot

#### `TapdataInit`

**Type:** `() -> Ctx8`

**Description:** Initialize taproot data structure

---

## Elements Jets

### Arithmetic Operations

#### `Add(8/16/32/64)`

**Type:** `(WordN, WordN) -> (Bit, WordN)`

**Description:** Addition of two n-bit words returning carry bit and sum

#### `Decrement(8/16/32/64)`

**Type:** `WordN -> (Bit, WordN)`

**Description:** Decrement n-bit word by 1 returning borrow bit and result

#### `DivMod(8/16/32/64)`

**Type:** `(WordN, WordN) -> (WordN, WordN)`

**Description:** Division and modulo of two n-bit words returning quotient and remainder

#### `DivMod128_64`

**Type:** `(Word128, Word64) -> (Word64, Word64)`

**Description:** Divide 128-bit word by 64-bit word returning quotient and remainder

#### `Divide(8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Division of two n-bit words returning quotient

#### `Divides(8/16/32/64)`

**Type:** `(WordN, WordN) -> Bit`

**Description:** Check if first n-bit word divides the second

#### `FeAdd`

**Type:** `(FE, FE) -> FE`

**Description:** Add two secp256k1 field elements

#### `FeMultiply`

**Type:** `(FE, FE) -> FE`

**Description:** Multiply two secp256k1 field elements

#### `FeMultiplyBeta`

**Type:** `FE -> FE`

**Description:** Multiply secp256k1 field element by beta constant

#### `FeNegate`

**Type:** `FE -> FE`

**Description:** Negate secp256k1 field element

#### `FullAdd(8/16/32/64)`

**Type:** `(Bit, (WordN, WordN)) -> (Bit, WordN)`

**Description:** Full adder with carry input for n-bit words

#### `FullDecrement(8/16/32/64)`

**Type:** `(Bit, WordN) -> (Bit, WordN)`

**Description:** Decrement with borrow input for n-bit words

#### `FullIncrement(8/16/32/64)`

**Type:** `(Bit, WordN) -> (Bit, WordN)`

**Description:** Increment with carry input for n-bit words

#### `FullMultiply(8/16/32/64)`

**Type:** `((WordN, WordN), (WordN, WordN)) -> Word(2N)`

**Description:** Multiply two n-bit words with two carry words producing 2n-bit result

#### `FullSubtract(8/16/32/64)`

**Type:** `(Bit, (WordN, WordN)) -> (Bit, WordN)`

**Description:** Full subtractor with borrow input for n-bit words

#### `GeNegate`

**Type:** `GE -> GE`

**Description:** Negate affine elliptic curve point

#### `GejAdd`

**Type:** `(GEJ, GEJ) -> GEJ`

**Description:** Add two Jacobian elliptic curve points

#### `GejGeAdd`

**Type:** `(GEJ, GE) -> GEJ`

**Description:** Add Jacobian point to affine point

#### `GejGeAddEx`

**Type:** `(GEJ, GE) -> (FE, GEJ)`

**Description:** Add Jacobian point to affine point with extra output

#### `GejNegate`

**Type:** `GEJ -> GEJ`

**Description:** Negate Jacobian elliptic curve point

#### `Increment(8/16/32/64)`

**Type:** `WordN -> (Bit, WordN)`

**Description:** Increment n-bit word by 1 returning carry bit and result

#### `Max(8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Return maximum of two n-bit words

#### `Median(8/16/32/64)`

**Type:** `(WordN, (WordN, WordN)) -> WordN`

**Description:** Return median value of three n-bit words

#### `Min(8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Return minimum of two n-bit words

#### `Modulo(8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Compute modulo (remainder) of first n-bit word divided by second

#### `Multiply(8/16/32/64)`

**Type:** `(WordN, WordN) -> Word(2N)`

**Description:** Multiply two n-bit words producing 2n-bit result

#### `Negate(8/16/32/64)`

**Type:** `WordN -> (Bit, WordN)`

**Description:** Two's complement negation of n-bit word

#### `ScalarAdd`

**Type:** `(Scalar, Scalar) -> Scalar`

**Description:** Add two secp256k1 scalars

#### `ScalarMultiply`

**Type:** `(Scalar, Scalar) -> Scalar`

**Description:** Multiply two secp256k1 scalars

#### `ScalarMultiplyLambda`

**Type:** `Scalar -> Scalar`

**Description:** Multiply secp256k1 scalar by lambda constant

#### `ScalarNegate`

**Type:** `Scalar -> Scalar`

**Description:** Negate secp256k1 scalar

#### `Sha256Ctx8Add(1/2/4/8/16/32/64/128/256/512)`

**Type:** `(Ctx8, WordN) -> Ctx8`

**Description:** Add n-bit data to SHA256 context

#### `Sha256Ctx8AddBuffer511`

**Type:** `(Ctx8, Buffer511) -> Ctx8`

**Description:** Add buffer up to 511 bytes to SHA256 context

#### `Subtract(8/16/32/64)`

**Type:** `(WordN, WordN) -> (Bit, WordN)`

**Description:** Subtraction of two n-bit words returning borrow bit and difference

### Bitwise Logic

#### `And(1/8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Bitwise AND of two n-bit words

#### `Ch(1/8/16/32/64)`

**Type:** `(WordN, (WordN, WordN)) -> WordN`

**Description:** Bitwise choice: for each bit position, if bit in first word is 1 choose from second word, else choose from third word

#### `CheckLockDistance`

**Description:** Verify that input's sequence uses block distance and matches

#### `CheckLockDuration`

**Description:** Verify that input's sequence uses time duration and matches

#### `CheckLockHeight`

**Description:** Verify that input's locktime uses block height and matches

#### `CheckLockTime`

**Description:** Verify that input's locktime uses block time and matches

#### `CheckSigVerify`

**Type:** `((PubKey, Word512), Sig) -> ()`

**Description:** Verify Schnorr signature and fail if invalid

#### `Complement(1/8/16/32/64)`

**Type:** `WordN -> WordN`

**Description:** Bitwise NOT (complement) of n-bit word

#### `Maj(1/8/16/32/64)`

**Type:** `(WordN, (WordN, WordN)) -> WordN`

**Description:** Majority function: returns bitwise majority of three n-bit words

#### `Or(1/8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Bitwise OR of two n-bit words

#### `Xor(1/8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Bitwise XOR of two n-bit words

#### `XorXor(1/8/16/32/64)`

**Type:** `(WordN, (WordN, WordN)) -> WordN`

**Description:** XOR of three n-bit words (a XOR b XOR c)

### Comparison & Testing

#### `All(8/16/32/64)`

**Type:** `WordN -> Bit`

**Description:** Test if all bits are set in n-bit word

#### `Eq(1/8/16/32/64/256)`

**Type:** `(WordN, WordN) -> Bit`

**Description:** Test equality of two n-bit words

#### `FeIsZero`

**Type:** `FE -> Bit`

**Description:** Test if secp256k1 field element is zero

#### `FullLeftShift16_(1/2/4/8)`

**Type:** `(Word16, WordK) -> (WordK, Word16)`

**Description:** Left shift 16-bit word by k bits returning shifted-out bits and result

#### `FullLeftShift32_(1/2/4/8/16)`

**Type:** `(Word32, WordK) -> (WordK, Word32)`

**Description:** Left shift 32-bit word by k bits returning shifted-out bits and result

#### `FullLeftShift64_(1/2/4/8/16/32)`

**Type:** `(Word64, WordK) -> (WordK, Word64)`

**Description:** Left shift 64-bit word by k bits returning shifted-out bits and result

#### `FullLeftShift8_(1/2/4)`

**Type:** `(Word8, WordK) -> (WordK, Word8)`

**Description:** Left shift 8-bit word by k bits returning shifted-out bits and result

#### `GejEquiv`

**Type:** `(GEJ, GEJ) -> Bit`

**Description:** Test equivalence of two Jacobian points

#### `GejGeEquiv`

**Type:** `(GEJ, GE) -> Bit`

**Description:** Test equivalence of Jacobian and affine points

#### `GejXEquiv`

**Type:** `(FE, GEJ) -> Bit`

**Description:** Test if Jacobian point has given x-coordinate

#### `IsOne(8/16/32/64)`

**Type:** `WordN -> Bit`

**Description:** Test if n-bit word is one

#### `IsZero(8/16/32/64)`

**Type:** `WordN -> Bit`

**Description:** Test if n-bit word is zero

#### `Le(8/16/32/64)`

**Type:** `(WordN, WordN) -> Bit`

**Description:** Test if first n-bit word is less than or equal to second

#### `LeftExtend16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Sign-extend 16-bit word to wider word by replicating the MSB on the left

#### `LeftExtend1_(8/16/32/64)`

**Type:** `Word1 -> WordN`

**Description:** Sign-extend 1-bit value to wider word by replicating the bit on the left

#### `LeftExtend32_64`

**Type:** `Word32 -> Word64`

**Description:** Sign-extend 32-bit word to 64-bit by replicating the MSB on the left

#### `LeftExtend8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Sign-extend 8-bit word to wider word by replicating the MSB on the left

#### `LeftPadHigh16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Pad 16-bit word to wider word with zeros on the right (high side)

#### `LeftPadHigh1_(8/16/32/64)`

**Type:** `Word1 -> WordN`

**Description:** Pad 1-bit value to wider word with zeros on the right (high side)

#### `LeftPadHigh32_64`

**Type:** `Word32 -> Word64`

**Description:** Pad 32-bit word to 64-bit with zeros on the right (high side)

#### `LeftPadHigh8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Pad 8-bit word to wider word with zeros on the right (high side)

#### `LeftPadLow16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Pad 16-bit word to wider word with zeros on the left (low side)

#### `LeftPadLow1_(8/16/32/64)`

**Type:** `Word1 -> WordN`

**Description:** Pad 1-bit value to wider word with zeros on the left (low side)

#### `LeftPadLow32_64`

**Type:** `Word32 -> Word64`

**Description:** Pad 32-bit word to 64-bit with zeros on the left (low side)

#### `LeftPadLow8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Pad 8-bit word to wider word with zeros on the left (low side)

#### `LeftRotate(8/16/32/64)`

**Type:** `(Word4/Word8, WordN) -> WordN`

**Description:** Left rotate (circular shift) n-bit word

#### `LeftShift(8/16/32/64)`

**Type:** `(Word4/Word8, WordN) -> WordN`

**Description:** Left shift n-bit word by specified amount

#### `LeftShiftWith(8/16/32/64)`

**Type:** `(Bit, (Word4/Word8, WordN)) -> WordN`

**Description:** Left shift n-bit word filling with specified bit

#### `Leftmost16_(1/2/4/8)`

**Type:** `Word16 -> WordK`

**Description:** Extract leftmost (most significant) k bits from 16-bit word

#### `Leftmost32_(1/2/4/8/16)`

**Type:** `Word32 -> WordK`

**Description:** Extract leftmost (most significant) k bits from 32-bit word

#### `Leftmost64_(1/2/4/8/16/32)`

**Type:** `Word64 -> WordK`

**Description:** Extract leftmost (most significant) k bits from 64-bit word

#### `Leftmost8_(1/2/4)`

**Type:** `Word8 -> WordK`

**Description:** Extract leftmost (most significant) k bits from 8-bit word

#### `Lt(8/16/32/64)`

**Type:** `(WordN, WordN) -> Bit`

**Description:** Test if first n-bit word is less than second

#### `ScalarIsZero`

**Type:** `Scalar -> Bit`

**Description:** Test if secp256k1 scalar is zero

#### `SigAllHash`

**Description:** Compute SIGHASH_ALL message hash

#### `Some(1/8/16/32/64)`

**Type:** `WordN -> Bit`

**Description:** Test if any bit is set in n-bit word (returns true if word is non-zero)

### Shift & Rotate

#### `FullRightShift16_(1/2/4/8)`

**Type:** `(WordK, Word16) -> (Word16, WordK)`

**Description:** Right shift 16-bit word by k bits returning result and shifted-out bits

#### `FullRightShift32_(1/2/4/8/16)`

**Type:** `(WordK, Word32) -> (Word32, WordK)`

**Description:** Right shift 32-bit word by k bits returning result and shifted-out bits

#### `FullRightShift64_(1/2/4/8/16/32)`

**Type:** `(WordK, Word64) -> (Word64, WordK)`

**Description:** Right shift 64-bit word by k bits returning result and shifted-out bits

#### `FullRightShift8_(1/2/4)`

**Type:** `(WordK, Word8) -> (Word8, WordK)`

**Description:** Right shift 8-bit word by k bits returning result and shifted-out bits

#### `RightRotate(8/16/32/64)`

**Type:** `(Word4/Word8, WordN) -> WordN`

**Description:** Right rotate (circular shift) n-bit word

#### `RightShift(8/16/32/64)`

**Type:** `(Word4/Word8, WordN) -> WordN`

**Description:** Right shift n-bit word by specified amount

#### `RightShiftWith(8/16/32/64)`

**Type:** `(Bit, (Word4/Word8, WordN)) -> WordN`

**Description:** Right shift n-bit word filling with specified bit

### Bit Manipulation

#### `RightExtend16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Sign-extend 16-bit word to wider word by replicating the LSB on the right

#### `RightExtend32_64`

**Type:** `Word32 -> Word64`

**Description:** Sign-extend 32-bit word to 64-bit by replicating the LSB on the right

#### `RightExtend8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Sign-extend 8-bit word to wider word by replicating the LSB on the right

#### `RightPadHigh16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Pad 16-bit word to wider word with zeros on the left (high side)

#### `RightPadHigh1_(8/16/32/64)`

**Type:** `Word1 -> WordN`

**Description:** Pad 1-bit value to wider word with zeros on the left (high side)

#### `RightPadHigh32_64`

**Type:** `Word32 -> Word64`

**Description:** Pad 32-bit word to 64-bit with zeros on the left (high side)

#### `RightPadHigh8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Pad 8-bit word to wider word with zeros on the left (high side)

#### `RightPadLow16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Pad 16-bit word to wider word with zeros on the right (low side)

#### `RightPadLow1_(8/16/32/64)`

**Type:** `Word1 -> WordN`

**Description:** Pad 1-bit value to wider word with zeros on the right (low side)

#### `RightPadLow32_64`

**Type:** `Word32 -> Word64`

**Description:** Pad 32-bit word to 64-bit with zeros on the right (low side)

#### `RightPadLow8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Pad 8-bit word to wider word with zeros on the right (low side)

#### `Rightmost16_(1/2/4/8)`

**Type:** `Word16 -> WordK`

**Description:** Extract rightmost (least significant) k bits from 16-bit word

#### `Rightmost32_(1/2/4/8/16)`

**Type:** `Word32 -> WordK`

**Description:** Extract rightmost (least significant) k bits from 32-bit word

#### `Rightmost64_(1/2/4/8/16/32)`

**Type:** `Word64 -> WordK`

**Description:** Extract rightmost (least significant) k bits from 64-bit word

#### `Rightmost8_(1/2/4)`

**Type:** `Word8 -> WordK`

**Description:** Extract rightmost (least significant) k bits from 8-bit word

### Constants

#### `High(1/8/16/32/64)`

**Type:** `() -> WordN`

**Description:** Constant word with all bits set to 1

#### `Low(1/8/16/32/64)`

**Type:** `() -> WordN`

**Description:** Constant word with all bits set to 0

#### `One(8/16/32/64)`

**Type:** `() -> WordN`

**Description:** Constant word with value 1

### Secp256k1 Field Elements

#### `FeInvert`

**Type:** `FE -> FE`

**Description:** Compute multiplicative inverse of secp256k1 field element

#### `FeIsOdd`

**Type:** `FE -> Bit`

**Description:** Test if secp256k1 field element is odd

#### `FeNormalize`

**Type:** `FE -> FE`

**Description:** Normalize secp256k1 field element to canonical form

#### `FeSquare`

**Type:** `FE -> FE`

**Description:** Square secp256k1 field element

#### `FeSquareRoot`

**Type:** `FE -> Maybe FE`

**Description:** Compute square root of secp256k1 field element if it exists

### Secp256k1 Scalars

#### `ScalarInvert`

**Type:** `Scalar -> Scalar`

**Description:** Compute multiplicative inverse of secp256k1 scalar

#### `ScalarNormalize`

**Type:** `Scalar -> Scalar`

**Description:** Normalize secp256k1 scalar to canonical form

#### `ScalarSquare`

**Type:** `Scalar -> Scalar`

**Description:** Square secp256k1 scalar

### Secp256k1 Points

#### `GeIsOnCurve`

**Type:** `GE -> Bit`

**Description:** Test if affine point is on the secp256k1 curve

#### `GejDouble`

**Type:** `GEJ -> GEJ`

**Description:** Double Jacobian elliptic curve point

#### `GejInfinity`

**Type:** `() -> GEJ`

**Description:** Create point at infinity in Jacobian coordinates

#### `GejIsInfinity`

**Type:** `GEJ -> Bit`

**Description:** Test if Jacobian point is at infinity

#### `GejIsOnCurve`

**Type:** `GEJ -> Bit`

**Description:** Test if Jacobian point is on the curve

#### `GejNormalize`

**Type:** `GEJ -> Maybe GE`

**Description:** Normalize Jacobian point to affine coordinates

#### `GejRescale`

**Type:** `(GEJ, FE) -> GEJ`

**Description:** Rescale Jacobian point by field element

#### `GejYIsOdd`

**Type:** `GEJ -> Bit`

**Description:** Test if y-coordinate of Jacobian point is odd

#### `Generate`

**Type:** `Scalar -> GEJ`

**Description:** Generate secp256k1 public key from scalar (scalar multiplication by generator point)

#### `GenesisBlockHash`

**Description:** Get genesis block hash for the blockchain

### Elliptic Curve Operations

#### `Decompress`

**Type:** `Point -> Maybe GE`

**Description:** Decompress secp256k1 public key from x-coordinate

#### `HashToCurve`

**Type:** `Word256 -> GE`

**Description:** Hash arbitrary data to curve point

#### `LinearCombination1`

**Type:** `((Scalar, GEJ), Scalar) -> GEJ`

**Description:** Compute s1*P1 + s2*G where s1,s2 are scalars, P1 is a point, G is generator

#### `LinearVerify1`

**Type:** `(((Scalar, GE), Scalar), GE) -> ()`

**Description:** Verify that s1*P1 + s2*P2 = point at infinity (linear combination check)

#### `PointVerify1`

**Type:** `(((Scalar, Point), Scalar), Point) -> ()`

**Description:** Verify Schnorr signature equation using linear combination

#### `Scale`

**Type:** `(Scalar, GEJ) -> GEJ`

**Description:** Scalar multiplication of curve point

#### `Swu`

**Type:** `FE -> GE`

**Description:** Shallue-van de Woestijne encoding to curve point

### Signatures

#### `Bip0340Verify`

**Type:** `((PubKey, Word256), Sig) -> ()`

**Description:** Verify BIP-340 Schnorr signature

#### `CurrentScriptSigHash`

**Type:** `() -> Word256`

**Description:** CurrentScriptSigHash operation (description not available)

#### `InputScriptSigHash`

**Type:** `Word32 -> Maybe Word256`

**Description:** Get scriptSig hash of specified input by index

#### `InputScriptSigsHash`

**Description:** Compute hash of all input scriptSigs

#### `Verify`

**Type:** `Bit -> ()`

**Description:** Assert that input bit is true (fail if false)

### SHA256 Hashing

#### `Sha256Block`

**Type:** `(Hash256, Block512) -> Hash256`

**Description:** Process single 512-bit block through SHA256 compression function

#### `Sha256Ctx8Finalize`

**Type:** `Ctx8 -> Hash256`

**Description:** Finalize SHA256 hash computation from context returning hash digest

#### `Sha256Ctx8Init`

**Type:** `() -> Ctx8`

**Description:** Initialize SHA256 context to initial state

#### `Sha256Iv`

**Type:** `() -> Hash256`

**Description:** Get SHA256 initial values

### Transaction Data

#### `CurrentAmount`

**Type:** `() -> (ConfWord256, ConfWord64)`

**Description:** Get confidential amount (value blinding, amount) of current input

#### `CurrentAsset`

**Type:** `() -> ConfWord256`

**Description:** Get confidential asset ID of current input

#### `CurrentIndex`

**Type:** `() -> Word32`

**Description:** Get index of current input being validated

#### `CurrentPegin`

**Type:** `() -> Maybe Word256`

**Description:** Get peg-in proof for current input (if applicable)

#### `CurrentPrevOutpoint`

**Type:** `() -> (Word256, Word32)`

**Description:** Get previous outpoint (txid, vout) of current input

#### `CurrentReissuanceBlinding`

**Description:** Get reissuance blinding nonce of current input

#### `CurrentReissuanceEntropy`

**Description:** Get reissuance entropy of current input

#### `CurrentSequence`

**Type:** `() -> Word32`

**Description:** Get sequence number of current input

#### `NumInputs`

**Type:** `() -> Word32`

**Description:** Get number of transaction inputs

#### `NumOutputs`

**Type:** `() -> Word32`

**Description:** Get number of transaction outputs

#### `TotalFee`

**Description:** Calculate total fee for specified asset

#### `TransactionId`

**Type:** `() -> Word256`

**Description:** Get current transaction ID

#### `Version`

**Type:** `() -> Word32`

**Description:** Get transaction version number

### Transaction Inputs

#### `InputAmount`

**Type:** `Word32 -> Maybe (ConfWord256, ConfWord64)`

**Description:** Get confidential amount of specified input by index

#### `InputAmountsHash`

**Description:** Compute hash of all input amounts

#### `InputAnnexHash`

**Type:** `Word32 -> Maybe Word256`

**Description:** Get annex hash of specified input by index

#### `InputAnnexesHash`

**Description:** Compute hash of all input annexes

#### `InputAsset`

**Type:** `Word32 -> Maybe ConfWord256`

**Description:** Get confidential asset ID of specified input by index

#### `InputHash`

**Description:** Compute hash of individual input

#### `InputOutpointsHash`

**Description:** Compute hash of all input outpoints

#### `InputPegin`

**Type:** `Word32 -> Maybe Word256`

**Description:** Get peg-in proof of specified input by index

#### `InputPrevOutpoint`

**Type:** `Word32 -> Maybe (Word256, Word32)`

**Description:** Get previous outpoint of specified input by index

#### `InputScriptHash`

**Type:** `Word32 -> Maybe Word256`

**Description:** Get script hash of specified input by index

#### `InputScriptsHash`

**Description:** Compute hash of all input scripts

#### `InputSequence`

**Type:** `Word32 -> Maybe Word32`

**Description:** Get sequence number of specified input by index

#### `InputSequencesHash`

**Description:** Compute hash of all input sequences

#### `InputUtxoHash`

**Description:** Compute hash of UTXO at specified input

#### `InputUtxosHash`

**Description:** Compute hash of all input UTXOs

#### `InputsHash`

**Description:** Compute hash of all transaction inputs

### Transaction Outputs

#### `OutputAmount`

**Type:** `Word32 -> Maybe (ConfWord256, ConfWord64)`

**Description:** Get confidential amount of specified output by index

#### `OutputAmountsHash`

**Description:** Compute hash of all output amounts

#### `OutputAsset`

**Type:** `Word32 -> Maybe ConfWord256`

**Description:** Get confidential asset ID of specified output by index

#### `OutputHash`

**Description:** Compute hash of individual output

#### `OutputIsFee`

**Type:** `Word32 -> Maybe Bit`

**Description:** Test if specified output is a fee output

#### `OutputNonce`

**Type:** `Word32 -> Maybe ConfWord256`

**Description:** Get confidential nonce of specified output by index

#### `OutputNoncesHash`

**Description:** Compute hash of all output nonces

#### `OutputNullDatum`

**Description:** Get null datum field of specified output by index

#### `OutputRangeProof`

**Description:** Get value range proof hash of specified output by index

#### `OutputRangeProofsHash`

**Description:** Compute hash of all output range proofs

#### `OutputScriptHash`

**Type:** `Word32 -> Maybe Word256`

**Description:** Get script hash of specified output by index

#### `OutputScriptsHash`

**Description:** Compute hash of all output scripts

#### `OutputSurjectionProof`

**Description:** Get asset surjection proof hash of specified output by index

#### `OutputSurjectionProofsHash`

**Description:** Compute hash of all output surjection proofs

#### `OutputsHash`

**Description:** Compute hash of all transaction outputs

### Issuance

#### `CalculateAsset`

**Description:** Calculate asset ID from entropy

#### `CalculateConfidentialToken`

**Description:** Calculate confidential reissuance token ID

#### `CalculateExplicitToken`

**Description:** Calculate explicit reissuance token ID

#### `CalculateIssuanceEntropy`

**Description:** Calculate issuance entropy from previous outpoint and contract hash

#### `CurrentIssuanceAssetAmount`

**Description:** Get issuance asset amount of current input

#### `CurrentIssuanceAssetProof`

**Description:** Get issuance asset range proof of current input

#### `CurrentIssuanceTokenAmount`

**Description:** Get issuance token amount of current input

#### `CurrentIssuanceTokenProof`

**Description:** Get issuance token range proof of current input

#### `CurrentNewIssuanceContract`

**Description:** Get new issuance contract hash of current input

#### `Issuance`

**Description:** Issuance operation (description not available)

#### `IssuanceAsset`

**Type:** `Word32 -> Maybe Word256`

**Description:** Get asset ID for specified issuance by input index

#### `IssuanceAssetAmount`

**Description:** Get asset amount for specified issuance by input index

#### `IssuanceAssetAmountsHash`

**Description:** Compute hash of all issuance asset amounts

#### `IssuanceAssetProof`

**Description:** Get asset amount range proof for specified issuance by input index

#### `IssuanceBlindingEntropyHash`

**Description:** Compute hash of all issuance blinding entropies

#### `IssuanceEntropy`

**Type:** `Word32 -> Maybe Word256`

**Description:** Get issuance entropy for specified issuance by input index

#### `IssuanceHash`

**Description:** Compute hash of individual issuance

#### `IssuanceRangeProofsHash`

**Description:** Compute hash of all issuance range proofs

#### `IssuanceToken`

**Type:** `Word32 -> Maybe Word256`

**Description:** Get reissuance token ID for specified issuance by input index

#### `IssuanceTokenAmount`

**Description:** Get token amount for specified issuance by input index

#### `IssuanceTokenAmountsHash`

**Description:** Compute hash of all issuance token amounts

#### `IssuanceTokenProof`

**Description:** Get token amount range proof for specified issuance by input index

#### `IssuancesHash`

**Description:** Compute hash of all issuances

#### `LbtcAsset`

**Description:** Get the L-BTC (Liquid Bitcoin) asset ID constant

#### `NewIssuanceContract`

**Description:** Get new issuance contract hash

### Time Locks

#### `LockTime`

**Type:** `() -> Word32`

**Description:** Get transaction lock time

#### `ParseLock`

**Type:** `Word32 -> Either Word32 Word32`

**Description:** Parse lock time from transaction data

#### `ParseSequence`

**Type:** `Word32 -> Maybe (Either Word16 Word16)`

**Description:** Parse sequence number from input data

#### `TxIsFinal`

**Type:** `() -> Bit`

**Description:** Test if transaction is final (all inputs have max sequence)

#### `TxLockDistance`

**Description:** Get transaction lock distance from sequence number

#### `TxLockDuration`

**Description:** Get transaction lock duration from sequence number

#### `TxLockHeight`

**Description:** Get transaction lock time as block height (if applicable)

#### `TxLockTime`

**Description:** Get transaction lock time as Unix timestamp (if applicable)

### Taproot

#### `AnnexHash`

**Description:** Compute hash of annex data

#### `BuildTapbranch`

**Description:** Compute taproot branch hash from two child hashes

#### `BuildTapleafSimplicity`

**Description:** Compute taproot leaf hash for Simplicity script

#### `BuildTaptweak`

**Description:** Compute taproot tweak from internal key and merkle root

#### `CurrentAnnexHash`

**Type:** `() -> Maybe Word256`

**Description:** CurrentAnnexHash operation (description not available)

#### `CurrentScriptHash`

**Type:** `() -> Word256`

**Description:** Get script hash of current input being validated

#### `InternalKey`

**Type:** `() -> PubKey`

**Description:** Get taproot internal public key

#### `ScriptCMR`

**Type:** `() -> Word256`

**Description:** Get commitment Merkle root of current script

#### `TapEnvHash`

**Description:** Compute taproot environment hash

#### `TapdataInit`

**Type:** `() -> Ctx8`

**Description:** Initialize taproot data structure

#### `TapleafHash`

**Description:** Compute hash of taproot leaf

#### `TapleafVersion`

**Type:** `() -> Word8`

**Description:** Get version byte of current taproot script leaf

#### `Tappath`

**Type:** `() -> Path`

**Description:** Get taproot script path

#### `TappathHash`

**Description:** Compute hash of taproot path

### Hash Operations

#### `AssetAmountHash`

**Description:** Compute hash of asset and amount pair

#### `NonceHash`

**Description:** Compute hash of nonce

#### `OutpointHash`

**Description:** Compute hash of outpoint

#### `TxHash`

**Description:** Compute transaction hash

### Other

#### `ReissuanceBlinding`

**Description:** Get reissuance blinding factor

#### `ReissuanceEntropy`

**Description:** Get reissuance entropy

---

## Bitcoin Jets

### Arithmetic Operations

#### `Add(8/16/32/64)`

**Type:** `(WordN, WordN) -> (Bit, WordN)`

**Description:** Addition of two n-bit words returning carry bit and sum

#### `Decrement(8/16/32/64)`

**Type:** `WordN -> (Bit, WordN)`

**Description:** Decrement n-bit word by 1 returning borrow bit and result

#### `DivMod(8/16/32/64)`

**Type:** `(WordN, WordN) -> (WordN, WordN)`

**Description:** Division and modulo of two n-bit words returning quotient and remainder

#### `DivMod128_64`

**Type:** `(Word128, Word64) -> (Word64, Word64)`

**Description:** Divide 128-bit word by 64-bit word returning quotient and remainder

#### `Divide(8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Division of two n-bit words returning quotient

#### `Divides(8/16/32/64)`

**Type:** `(WordN, WordN) -> Bit`

**Description:** Check if first n-bit word divides the second

#### `FeAdd`

**Type:** `(FE, FE) -> FE`

**Description:** Add two secp256k1 field elements

#### `FeMultiply`

**Type:** `(FE, FE) -> FE`

**Description:** Multiply two secp256k1 field elements

#### `FeMultiplyBeta`

**Type:** `FE -> FE`

**Description:** Multiply secp256k1 field element by beta constant

#### `FeNegate`

**Type:** `FE -> FE`

**Description:** Negate secp256k1 field element

#### `FullAdd(8/16/32/64)`

**Type:** `(Bit, (WordN, WordN)) -> (Bit, WordN)`

**Description:** Full adder with carry input for n-bit words

#### `FullDecrement(8/16/32/64)`

**Type:** `(Bit, WordN) -> (Bit, WordN)`

**Description:** Decrement with borrow input for n-bit words

#### `FullIncrement(8/16/32/64)`

**Type:** `(Bit, WordN) -> (Bit, WordN)`

**Description:** Increment with carry input for n-bit words

#### `FullMultiply(8/16/32/64)`

**Type:** `((WordN, WordN), (WordN, WordN)) -> Word(2N)`

**Description:** Multiply two n-bit words with two carry words producing 2n-bit result

#### `FullSubtract(8/16/32/64)`

**Type:** `(Bit, (WordN, WordN)) -> (Bit, WordN)`

**Description:** Full subtractor with borrow input for n-bit words

#### `GeNegate`

**Type:** `GE -> GE`

**Description:** Negate affine elliptic curve point

#### `GejAdd`

**Type:** `(GEJ, GEJ) -> GEJ`

**Description:** Add two Jacobian elliptic curve points

#### `GejGeAdd`

**Type:** `(GEJ, GE) -> GEJ`

**Description:** Add Jacobian point to affine point

#### `GejGeAddEx`

**Type:** `(GEJ, GE) -> (FE, GEJ)`

**Description:** Add Jacobian point to affine point with extra output

#### `GejNegate`

**Type:** `GEJ -> GEJ`

**Description:** Negate Jacobian elliptic curve point

#### `Increment(8/16/32/64)`

**Type:** `WordN -> (Bit, WordN)`

**Description:** Increment n-bit word by 1 returning carry bit and result

#### `Max(8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Return maximum of two n-bit words

#### `Median(8/16/32/64)`

**Type:** `(WordN, (WordN, WordN)) -> WordN`

**Description:** Return median value of three n-bit words

#### `Min(8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Return minimum of two n-bit words

#### `Modulo(8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Compute modulo (remainder) of first n-bit word divided by second

#### `Multiply(8/16/32/64)`

**Type:** `(WordN, WordN) -> Word(2N)`

**Description:** Multiply two n-bit words producing 2n-bit result

#### `Negate(8/16/32/64)`

**Type:** `WordN -> (Bit, WordN)`

**Description:** Two's complement negation of n-bit word

#### `ScalarAdd`

**Type:** `(Scalar, Scalar) -> Scalar`

**Description:** Add two secp256k1 scalars

#### `ScalarMultiply`

**Type:** `(Scalar, Scalar) -> Scalar`

**Description:** Multiply two secp256k1 scalars

#### `ScalarMultiplyLambda`

**Type:** `Scalar -> Scalar`

**Description:** Multiply secp256k1 scalar by lambda constant

#### `ScalarNegate`

**Type:** `Scalar -> Scalar`

**Description:** Negate secp256k1 scalar

#### `Sha256Ctx8Add(1/2/4/8/16/32/64/128/256/512)`

**Type:** `(Ctx8, WordN) -> Ctx8`

**Description:** Add n-bit data to SHA256 context

#### `Sha256Ctx8AddBuffer511`

**Type:** `(Ctx8, Buffer511) -> Ctx8`

**Description:** Add buffer up to 511 bytes to SHA256 context

#### `Subtract(8/16/32/64)`

**Type:** `(WordN, WordN) -> (Bit, WordN)`

**Description:** Subtraction of two n-bit words returning borrow bit and difference

### Bitwise Logic

#### `And(1/8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Bitwise AND of two n-bit words

#### `Ch(1/8/16/32/64)`

**Type:** `(WordN, (WordN, WordN)) -> WordN`

**Description:** Bitwise choice: for each bit position, if bit in first word is 1 choose from second word, else choose from third word

#### `CheckLockDistance`

**Description:** Verify that input's sequence uses block distance and matches

#### `CheckLockDuration`

**Description:** Verify that input's sequence uses time duration and matches

#### `CheckLockHeight`

**Description:** Verify that input's locktime uses block height and matches

#### `CheckLockTime`

**Description:** Verify that input's locktime uses block time and matches

#### `CheckSigVerify`

**Type:** `((PubKey, Word512), Sig) -> ()`

**Description:** Verify Schnorr signature and fail if invalid

#### `Complement(1/8/16/32/64)`

**Type:** `WordN -> WordN`

**Description:** Bitwise NOT (complement) of n-bit word

#### `Maj(1/8/16/32/64)`

**Type:** `(WordN, (WordN, WordN)) -> WordN`

**Description:** Majority function: returns bitwise majority of three n-bit words

#### `Or(1/8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Bitwise OR of two n-bit words

#### `Xor(1/8/16/32/64)`

**Type:** `(WordN, WordN) -> WordN`

**Description:** Bitwise XOR of two n-bit words

#### `XorXor(1/8/16/32/64)`

**Type:** `(WordN, (WordN, WordN)) -> WordN`

**Description:** XOR of three n-bit words (a XOR b XOR c)

### Comparison & Testing

#### `All(8/16/32/64)`

**Type:** `WordN -> Bit`

**Description:** Test if all bits are set in n-bit word

#### `Eq(1/8/16/32/64/256)`

**Type:** `(WordN, WordN) -> Bit`

**Description:** Test equality of two n-bit words

#### `FeIsZero`

**Type:** `FE -> Bit`

**Description:** Test if secp256k1 field element is zero

#### `FullLeftShift16_(1/2/4/8)`

**Type:** `(Word16, WordK) -> (WordK, Word16)`

**Description:** Left shift 16-bit word by k bits returning shifted-out bits and result

#### `FullLeftShift32_(1/2/4/8/16)`

**Type:** `(Word32, WordK) -> (WordK, Word32)`

**Description:** Left shift 32-bit word by k bits returning shifted-out bits and result

#### `FullLeftShift64_(1/2/4/8/16/32)`

**Type:** `(Word64, WordK) -> (WordK, Word64)`

**Description:** Left shift 64-bit word by k bits returning shifted-out bits and result

#### `FullLeftShift8_(1/2/4)`

**Type:** `(Word8, WordK) -> (WordK, Word8)`

**Description:** Left shift 8-bit word by k bits returning shifted-out bits and result

#### `GejEquiv`

**Type:** `(GEJ, GEJ) -> Bit`

**Description:** Test equivalence of two Jacobian points

#### `GejGeEquiv`

**Type:** `(GEJ, GE) -> Bit`

**Description:** Test equivalence of Jacobian and affine points

#### `GejXEquiv`

**Type:** `(FE, GEJ) -> Bit`

**Description:** Test if Jacobian point has given x-coordinate

#### `IsOne(8/16/32/64)`

**Type:** `WordN -> Bit`

**Description:** Test if n-bit word is one

#### `IsZero(8/16/32/64)`

**Type:** `WordN -> Bit`

**Description:** Test if n-bit word is zero

#### `Le(8/16/32/64)`

**Type:** `(WordN, WordN) -> Bit`

**Description:** Test if first n-bit word is less than or equal to second

#### `LeftExtend16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Sign-extend 16-bit word to wider word by replicating the MSB on the left

#### `LeftExtend1_(8/16/32/64)`

**Type:** `Word1 -> WordN`

**Description:** Sign-extend 1-bit value to wider word by replicating the bit on the left

#### `LeftExtend32_64`

**Type:** `Word32 -> Word64`

**Description:** Sign-extend 32-bit word to 64-bit by replicating the MSB on the left

#### `LeftExtend8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Sign-extend 8-bit word to wider word by replicating the MSB on the left

#### `LeftPadHigh16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Pad 16-bit word to wider word with zeros on the right (high side)

#### `LeftPadHigh1_(8/16/32/64)`

**Type:** `Word1 -> WordN`

**Description:** Pad 1-bit value to wider word with zeros on the right (high side)

#### `LeftPadHigh32_64`

**Type:** `Word32 -> Word64`

**Description:** Pad 32-bit word to 64-bit with zeros on the right (high side)

#### `LeftPadHigh8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Pad 8-bit word to wider word with zeros on the right (high side)

#### `LeftPadLow16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Pad 16-bit word to wider word with zeros on the left (low side)

#### `LeftPadLow1_(8/16/32/64)`

**Type:** `Word1 -> WordN`

**Description:** Pad 1-bit value to wider word with zeros on the left (low side)

#### `LeftPadLow32_64`

**Type:** `Word32 -> Word64`

**Description:** Pad 32-bit word to 64-bit with zeros on the left (low side)

#### `LeftPadLow8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Pad 8-bit word to wider word with zeros on the left (low side)

#### `LeftRotate(8/16/32/64)`

**Type:** `(Word4/Word8, WordN) -> WordN`

**Description:** Left rotate (circular shift) n-bit word

#### `LeftShift(8/16/32/64)`

**Type:** `(Word4/Word8, WordN) -> WordN`

**Description:** Left shift n-bit word by specified amount

#### `LeftShiftWith(8/16/32/64)`

**Type:** `(Bit, (Word4/Word8, WordN)) -> WordN`

**Description:** Left shift n-bit word filling with specified bit

#### `Leftmost16_(1/2/4/8)`

**Type:** `Word16 -> WordK`

**Description:** Extract leftmost (most significant) k bits from 16-bit word

#### `Leftmost32_(1/2/4/8/16)`

**Type:** `Word32 -> WordK`

**Description:** Extract leftmost (most significant) k bits from 32-bit word

#### `Leftmost64_(1/2/4/8/16/32)`

**Type:** `Word64 -> WordK`

**Description:** Extract leftmost (most significant) k bits from 64-bit word

#### `Leftmost8_(1/2/4)`

**Type:** `Word8 -> WordK`

**Description:** Extract leftmost (most significant) k bits from 8-bit word

#### `Lt(8/16/32/64)`

**Type:** `(WordN, WordN) -> Bit`

**Description:** Test if first n-bit word is less than second

#### `ScalarIsZero`

**Type:** `Scalar -> Bit`

**Description:** Test if secp256k1 scalar is zero

#### `Some(1/8/16/32/64)`

**Type:** `WordN -> Bit`

**Description:** Test if any bit is set in n-bit word (returns true if word is non-zero)

### Shift & Rotate

#### `FullRightShift16_(1/2/4/8)`

**Type:** `(WordK, Word16) -> (Word16, WordK)`

**Description:** Right shift 16-bit word by k bits returning result and shifted-out bits

#### `FullRightShift32_(1/2/4/8/16)`

**Type:** `(WordK, Word32) -> (Word32, WordK)`

**Description:** Right shift 32-bit word by k bits returning result and shifted-out bits

#### `FullRightShift64_(1/2/4/8/16/32)`

**Type:** `(WordK, Word64) -> (Word64, WordK)`

**Description:** Right shift 64-bit word by k bits returning result and shifted-out bits

#### `FullRightShift8_(1/2/4)`

**Type:** `(WordK, Word8) -> (Word8, WordK)`

**Description:** Right shift 8-bit word by k bits returning result and shifted-out bits

#### `RightRotate(8/16/32/64)`

**Type:** `(Word4/Word8, WordN) -> WordN`

**Description:** Right rotate (circular shift) n-bit word

#### `RightShift(8/16/32/64)`

**Type:** `(Word4/Word8, WordN) -> WordN`

**Description:** Right shift n-bit word by specified amount

#### `RightShiftWith(8/16/32/64)`

**Type:** `(Bit, (Word4/Word8, WordN)) -> WordN`

**Description:** Right shift n-bit word filling with specified bit

### Bit Manipulation

#### `RightExtend16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Sign-extend 16-bit word to wider word by replicating the LSB on the right

#### `RightExtend32_64`

**Type:** `Word32 -> Word64`

**Description:** Sign-extend 32-bit word to 64-bit by replicating the LSB on the right

#### `RightExtend8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Sign-extend 8-bit word to wider word by replicating the LSB on the right

#### `RightPadHigh16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Pad 16-bit word to wider word with zeros on the left (high side)

#### `RightPadHigh1_(8/16/32/64)`

**Type:** `Word1 -> WordN`

**Description:** Pad 1-bit value to wider word with zeros on the left (high side)

#### `RightPadHigh32_64`

**Type:** `Word32 -> Word64`

**Description:** Pad 32-bit word to 64-bit with zeros on the left (high side)

#### `RightPadHigh8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Pad 8-bit word to wider word with zeros on the left (high side)

#### `RightPadLow16_(32/64)`

**Type:** `Word16 -> WordN`

**Description:** Pad 16-bit word to wider word with zeros on the right (low side)

#### `RightPadLow1_(8/16/32/64)`

**Type:** `Word1 -> WordN`

**Description:** Pad 1-bit value to wider word with zeros on the right (low side)

#### `RightPadLow32_64`

**Type:** `Word32 -> Word64`

**Description:** Pad 32-bit word to 64-bit with zeros on the right (low side)

#### `RightPadLow8_(16/32/64)`

**Type:** `Word8 -> WordN`

**Description:** Pad 8-bit word to wider word with zeros on the right (low side)

#### `Rightmost16_(1/2/4/8)`

**Type:** `Word16 -> WordK`

**Description:** Extract rightmost (least significant) k bits from 16-bit word

#### `Rightmost32_(1/2/4/8/16)`

**Type:** `Word32 -> WordK`

**Description:** Extract rightmost (least significant) k bits from 32-bit word

#### `Rightmost64_(1/2/4/8/16/32)`

**Type:** `Word64 -> WordK`

**Description:** Extract rightmost (least significant) k bits from 64-bit word

#### `Rightmost8_(1/2/4)`

**Type:** `Word8 -> WordK`

**Description:** Extract rightmost (least significant) k bits from 8-bit word

### Constants

#### `High(1/8/16/32/64)`

**Type:** `() -> WordN`

**Description:** Constant word with all bits set to 1

#### `Low(1/8/16/32/64)`

**Type:** `() -> WordN`

**Description:** Constant word with all bits set to 0

#### `One(8/16/32/64)`

**Type:** `() -> WordN`

**Description:** Constant word with value 1

### Secp256k1 Field Elements

#### `FeInvert`

**Type:** `FE -> FE`

**Description:** Compute multiplicative inverse of secp256k1 field element

#### `FeIsOdd`

**Type:** `FE -> Bit`

**Description:** Test if secp256k1 field element is odd

#### `FeNormalize`

**Type:** `FE -> FE`

**Description:** Normalize secp256k1 field element to canonical form

#### `FeSquare`

**Type:** `FE -> FE`

**Description:** Square secp256k1 field element

#### `FeSquareRoot`

**Type:** `FE -> Maybe FE`

**Description:** Compute square root of secp256k1 field element if it exists

### Secp256k1 Scalars

#### `ScalarInvert`

**Type:** `Scalar -> Scalar`

**Description:** Compute multiplicative inverse of secp256k1 scalar

#### `ScalarNormalize`

**Type:** `Scalar -> Scalar`

**Description:** Normalize secp256k1 scalar to canonical form

#### `ScalarSquare`

**Type:** `Scalar -> Scalar`

**Description:** Square secp256k1 scalar

### Secp256k1 Points

#### `GeIsOnCurve`

**Type:** `GE -> Bit`

**Description:** Test if affine point is on the secp256k1 curve

#### `GejDouble`

**Type:** `GEJ -> GEJ`

**Description:** Double Jacobian elliptic curve point

#### `GejInfinity`

**Type:** `() -> GEJ`

**Description:** Create point at infinity in Jacobian coordinates

#### `GejIsInfinity`

**Type:** `GEJ -> Bit`

**Description:** Test if Jacobian point is at infinity

#### `GejIsOnCurve`

**Type:** `GEJ -> Bit`

**Description:** Test if Jacobian point is on the curve

#### `GejNormalize`

**Type:** `GEJ -> Maybe GE`

**Description:** Normalize Jacobian point to affine coordinates

#### `GejRescale`

**Type:** `(GEJ, FE) -> GEJ`

**Description:** Rescale Jacobian point by field element

#### `GejYIsOdd`

**Type:** `GEJ -> Bit`

**Description:** Test if y-coordinate of Jacobian point is odd

#### `Generate`

**Type:** `Scalar -> GEJ`

**Description:** Generate secp256k1 public key from scalar (scalar multiplication by generator point)

### Elliptic Curve Operations

#### `Decompress`

**Type:** `Point -> Maybe GE`

**Description:** Decompress secp256k1 public key from x-coordinate

#### `HashToCurve`

**Type:** `Word256 -> GE`

**Description:** Hash arbitrary data to curve point

#### `LinearCombination1`

**Type:** `((Scalar, GEJ), Scalar) -> GEJ`

**Description:** Compute s1*P1 + s2*G where s1,s2 are scalars, P1 is a point, G is generator

#### `LinearVerify1`

**Type:** `(((Scalar, GE), Scalar), GE) -> ()`

**Description:** Verify that s1*P1 + s2*P2 = point at infinity (linear combination check)

#### `PointVerify1`

**Type:** `(((Scalar, Point), Scalar), Point) -> ()`

**Description:** Verify Schnorr signature equation using linear combination

#### `Scale`

**Type:** `(Scalar, GEJ) -> GEJ`

**Description:** Scalar multiplication of curve point

#### `Swu`

**Type:** `FE -> GE`

**Description:** Shallue-van de Woestijne encoding to curve point

### Signatures

#### `Bip0340Verify`

**Type:** `((PubKey, Word256), Sig) -> ()`

**Description:** Verify BIP-340 Schnorr signature

#### `CurrentScriptSigHash`

**Type:** `() -> Word256`

**Description:** CurrentScriptSigHash operation (description not available)

#### `InputScriptSigHash`

**Type:** `Word32 -> Maybe Word256`

**Description:** Get scriptSig hash of specified input by index

#### `Verify`

**Type:** `Bit -> ()`

**Description:** Assert that input bit is true (fail if false)

### SHA256 Hashing

#### `Sha256Block`

**Type:** `(Hash256, Block512) -> Hash256`

**Description:** Process single 512-bit block through SHA256 compression function

#### `Sha256Ctx8Finalize`

**Type:** `Ctx8 -> Hash256`

**Description:** Finalize SHA256 hash computation from context returning hash digest

#### `Sha256Ctx8Init`

**Type:** `() -> Ctx8`

**Description:** Initialize SHA256 context to initial state

#### `Sha256Iv`

**Type:** `() -> Hash256`

**Description:** Get SHA256 initial values

### Transaction Data

#### `CurrentIndex`

**Type:** `() -> Word32`

**Description:** Get index of current input being validated

#### `CurrentPrevOutpoint`

**Type:** `() -> (Word256, Word32)`

**Description:** Get previous outpoint (txid, vout) of current input

#### `CurrentSequence`

**Type:** `() -> Word32`

**Description:** Get sequence number of current input

#### `CurrentValue`

**Description:** Get value of current input being validated

#### `NumInputs`

**Type:** `() -> Word32`

**Description:** Get number of transaction inputs

#### `NumOutputs`

**Type:** `() -> Word32`

**Description:** Get number of transaction outputs

#### `TotalInputValue`

**Description:** Calculate total value of all transaction inputs

#### `TotalOutputValue`

**Description:** Calculate total value of all transaction outputs

#### `Version`

**Type:** `() -> Word32`

**Description:** Get transaction version number

### Transaction Inputs

#### `InputAnnexHash`

**Type:** `Word32 -> Maybe Word256`

**Description:** Get annex hash of specified input by index

#### `InputPrevOutpoint`

**Type:** `Word32 -> Maybe (Word256, Word32)`

**Description:** Get previous outpoint of specified input by index

#### `InputSequence`

**Type:** `Word32 -> Maybe Word32`

**Description:** Get sequence number of specified input by index

#### `InputValue`

**Type:** `Word32 -> Maybe Word64`

**Description:** Get value of specified input by index

### Transaction Outputs

#### `OutputScriptHash`

**Type:** `Word32 -> Maybe Word256`

**Description:** Get script hash of specified output by index

#### `OutputValue`

**Type:** `Word32 -> Maybe Word64`

**Description:** Get value of specified output by index

### Time Locks

#### `LockTime`

**Type:** `() -> Word32`

**Description:** Get transaction lock time

#### `ParseLock`

**Type:** `Word32 -> Either Word32 Word32`

**Description:** Parse lock time from transaction data

#### `ParseSequence`

**Type:** `Word32 -> Maybe (Either Word16 Word16)`

**Description:** Parse sequence number from input data

#### `TxIsFinal`

**Type:** `() -> Bit`

**Description:** Test if transaction is final (all inputs have max sequence)

#### `TxLockDistance`

**Description:** Get transaction lock distance from sequence number

#### `TxLockDuration`

**Description:** Get transaction lock duration from sequence number

#### `TxLockHeight`

**Description:** Get transaction lock time as block height (if applicable)

#### `TxLockTime`

**Description:** Get transaction lock time as Unix timestamp (if applicable)

### Taproot

#### `CurrentAnnexHash`

**Type:** `() -> Maybe Word256`

**Description:** CurrentAnnexHash operation (description not available)

#### `InternalKey`

**Type:** `() -> PubKey`

**Description:** Get taproot internal public key

#### `ScriptCMR`

**Type:** `() -> Word256`

**Description:** Get commitment Merkle root of current script

#### `TapdataInit`

**Type:** `() -> Ctx8`

**Description:** Initialize taproot data structure

#### `TapleafVersion`

**Type:** `() -> Word8`

**Description:** Get version byte of current taproot script leaf

#### `Tappath`

**Type:** `() -> Path`

**Description:** Get taproot script path

### Type Safety

**No type confusion** - Can't pass Word8 where Word32 expected  
**No buffer overflows** - Sizes checked at compile time  
**No null pointer errors** - `Maybe` type makes optionality explicit  
**No implicit conversions** - Must use explicit pad/extend jets  