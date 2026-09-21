package main
import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/sha1"
	"fmt"
)
func main() {
	// VULNERABLE TO QUANTUM: ECDSA P-256
	privKey, err := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
	if err != nil {
		panic(err)
	}
	fmt.Printf("Generated ECDSA key for curve: %s\n", privKey.Params().Name)
// VULNERABLE: SHA-1 usage
	hasher := sha1.New()
	hasher.Write([]byte("sample transaction data"))
	sha1Sum := hasher.Sum(nil)
	fmt.Printf("SHA1 Digest: %x\n", sha1Sum)
}
