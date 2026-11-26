# Exact visibility of the boundary wall under the original caps

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The lower-total wall of the shared Casimir equation has an explicit
trilinear current. Its contraction with the Frobenius cap is a bounded
weighted reversal, and its contraction with the ordinary marked cap
is zero. More generally its only invisible full cap vectors form one
specified line. Every other cap coordinate can be detected with only
a polynomial loss.

These statements apply to caps propagated through actual short words,
with their original order and phases. Multiplication preserves the
invisible line; a genuine turn exchanges it with the visible unit.
A single signed crossing already gives an exponentially large wall
operator from the unit cap. Thus the bounded bare-cap statement must
be used at its actual attachment, rather than assumed invariant under
an arbitrary short exterior.

## 1. The exact signed wall current

Fix \(N\ge2\), and put
\[
 d=N-1,\quad q=e^{\pi i/N},\quad
 \kappa=q^{d^2/2},\qquad
 s_r=2\sin(\pi r/N),\quad
 S_r=\prod_{h=1}^r s_h,\quad S_0=1 .
 \tag{1}
\]
Use the entire original algebra \(\mathcal H_N\), its Newton basis
\(e_0,\ldots,e_d\), and its positive coefficient norm. The original
closures and turn are
\[
 e_0=1,\quad \phi(e_ie_j)=\delta_{i+j,d},\quad
 \phi(e_i)=\delta_{i,d},\quad m(e_i)=\delta_{i,0},
 \qquad Je_i=e_{d-i}.
 \tag{2}
\]
The actual Casimir coordinate, denoted \(z\), obeys
\[
 ze_i=c_ie_i-s_{i+1}^2e_{i+1},
 \qquad c_i=2\cos((2i+1)\pi/N),
 \tag{3}
\]
where the last term is absent at \(i=d\).
The positive Newton triple tensor \(\tau_{ijk}=\phi(e_ie_je_k)\)
vanishes unless
\[
            i+j,\ i+k,\ j+k\le d,\qquad i+j+k\ge d ,
 \tag{4}
\]
and on that support is
\[
 \tau_{ijk}=
   \frac{S_{i+j}S_{i+k}S_{j+k}}
        {N S_iS_jS_kS_{i+j+k-d}} .
 \tag{5}
\]
Retain \(S_rS_{d-r}=N\).

If \(i+j+k=d-1\), (3)--(5) give
\[
 \begin{split}
 \phi(ze_ie_je_k)
   &=-s_{i+1}^2\tau_{i+1,j,k}\\
   &=-\frac{N^2}{S_i^2S_j^2S_k^2}.
 \end{split}
 \tag{6}
\]
Indeed all pair sums for the shifted triple are at most \(d\);
its total is \(d\), and complementary factorials in (5) give
\(\tau_{i+1,j,k}=N^2/(S_{i+1}^2S_j^2S_k^2)\).
This also proves that the result is independent of which leg
receives the Casimir.

For full packets \(A=\sum A_ie_i\), \(B=\sum B_je_j\),
\(C=\sum C_ke_k\), define precisely this wall part:
\[
 \boxed{\quad
 \mathcal W_N(A,B,C)
     =-N^2\sum_{i+j+k=d-1}
             \frac{A_iB_jC_k}{S_i^2S_j^2S_k^2}.
 \quad}
 \tag{7}
\]
It is a symmetric complex trilinear form. It is not asserted to be
the entire insertion \(\phi(zABC)\).
The shared-Casimir theorem identifies its sampled current as
\(N^{3/2}\gamma_i\gamma_j\gamma_k\) times (6), with the exact
unit phases \(\gamma\) of that theorem. Thus (7) retains the signed
original source normalization.

## 2. Both original caps and the full visibility criterion

For a cap vector \(v=\sum v_ie_i\), let
\[
                 W_v(A,B)=\mathcal W_N(v,A,B).
 \tag{8}
\]
Give this bilinear form its operator norm
\(\sup_{\|A\|=\|B\|=1}|W_v(A,B)|\), with no conjugation in
the bilinear form. This equals the usual singular-value norm
of its coefficient matrix.

**Theorem 1.** The Frobenius cap has dual vector \(1=e_0\), and
\[
 W_1(A,B)
       =-\sum_{j=0}^{d-1}s_{j+1}^2A_jB_{d-1-j},\qquad
             \|W_1\|=\max_{1\le r<N}s_r^2\le4.
 \tag{9}
\]
The ordinary marked cap has Frobenius-dual vector \(e_d\), and
\[
                            W_{e_d}=0 .
 \tag{10}
\]
For every full vector \(v\),
\[
 \boxed{\quad
 W_v=0\ \Longleftrightarrow\ v\in\mathbb C e_d,\qquad
 \|W_v\|\ge\frac{16}{N^2}
                      \left(\sum_{i=0}^{d-1}|v_i|^2\right)^{1/2}.
 \quad}
 \tag{11}
\]

**Proof.** In (7), setting the first input to \(e_0\) leaves
\(j+k=d-1\). Since \(S_{d-1-j}=N/S_{j+1}\), its coefficient
is \(-s_{j+1}^2\), proving (9). Setting that input to \(e_d\)
leaves no permitted triple, proving (10). Equation (2) proves
\(\phi(e_dA)=m(A)\), so these are the two original caps.

For arbitrary \(v\), a specified first row of its wall matrix is
\[
        W_v(e_0,e_{d-1-i})=-s_{i+1}^2v_i,
                         \qquad 0\le i<d .
 \tag{12}
\]
The Euclidean norm of a matrix row is at most its operator norm.
Moreover
\[
 s_r^2\ge4\sin^2(\pi/N)\ge16/N^2
                              \quad(1\le r<N);
 \tag{13}
\]
the last inequality follows from the chord bound for sine on
\([0,\pi/2]\). Thus (12) proves the lower bound in (11).
It also proves necessity in the kernel assertion; sufficiency
is (10). \(\square\)

For reference, the entire matrix is explicitly
\[
 (W_v)_{jk}=
 \begin{cases}
 \displaystyle
 -\frac{N^2v_{d-1-j-k}}
 {S_{d-1-j-k}^2S_j^2S_k^2},&j+k\le d-1,\\
 0,&j+k>d-1.
 \end{cases}
 \tag{14}
\]
Equivalently, if
\(\widehat A(t)=\sum_i A_it^i/S_i^2\), and similarly for other
inputs, then
\[
       \mathcal W_N(A,B,C)
          =-N^2[t^{d-1}]\,\widehat A(t)\widehat B(t)\widehat C(t).
 \tag{15}
\]
Equations (12) and (14) describe every cap direction, without
assuming that it is geometric or supplied by a particular word.
The first-row probes also have a direct original-source expression:
\[
        W_v(e_0,e_k)=\phi\!\left(v(z-c_k)e_k\right),
                                  \qquad0\le k<d .
 \tag{15a}
\]
Indeed \((z-c_k)e_k=-s_{k+1}^2e_{k+1}\), and (2) gives
the stated row; \(s_{k+1}=s_{d-k}\).
These are corrected full Newton coupons, not a replacement by
ordinary irreducible-color circles.

The first row also defines a known positive observation energy:
\[
 \begin{split}
 E_{\rm wall}(v)
   &=\sum_{j=0}^{d-1}|W_v(e_0,e_j)|^2
     =\sum_{i=0}^{d-1}s_{i+1}^4|v_i|^2,\\
 \frac{256}{N^4}\|P_{<d}v\|^2
   &\le E_{\rm wall}(v)\le16\|P_{<d}v\|^2 .
 \end{split}
 \tag{15b}
\]
Its Gram matrix is diagonal, with kernel exactly \(\mathbb C e_d\).
This is an observation energy, not an upper bound on \(\|W_v\|\).
Also \(\phi(e_d)=1\): that line cannot be discarded from the
original full source just because this observation misses it.
If a full norm is desired, the explicitly retained original row
completes it to
\[
 E_{\rm wall}(v)+|\phi(v)|^2
     =\sum_{i<d}s_{i+1}^4|v_i|^2+|v_d|^2 .
 \tag{15c}
\]
The comparison constants with the Newton norm are at worst polynomial
in \(N\); no replacement of the original scalar closing is asserted.

## 3. Actual short words and their order

Let \(M_B\) denote multiplication by any actual full packet \(B\),
and let \(T\) be a finite composition of such operators and the
genuine turn \(J\). All scalar and framing factors in \(B\) remain
part of \(M_B\). Define the adjoint here for the original bilinear
Frobenius form:
\[
               \phi((TX)Y)=\phi(X(T^\dagger Y)).
 \tag{16}
\]
It is not a Hermitian adjoint. Associativity and commutativity give
\(M_B^\dagger=M_B\). Also \(J^\dagger=J\): in Newton coordinates
the Frobenius matrix and the turn are both the reversal matrix,
which is symmetric and squares to the identity.
Consequently the adjoint of a word reverses its operator order,
without conjugating its coefficients.

The propagated original caps are therefore exactly
\[
 \phi(TX)=\phi(v_\phi X),\quad v_\phi=T^\dagger1,\qquad
 m(TX)=\phi(v_mX),\quad v_m=T^\dagger e_d .
 \tag{17}
\]
Theorem 1 applies to these full vectors, for every such word.
There is no new closure or renormalized scalar in (17).
Its computation may require the entire short boundary packet;
the result makes no claim that its coefficients are cheaply known.

There is a useful invariant line under every multiplication coupon:
\[
                         e_dB=m(B)e_d .
 \tag{18}
\]
Indeed \(e_de_j=0\) for \(j\ge1\), by the original positive
multiplication support, and \(e_de_0=e_d\).
The scalar \(m(B)\) is allowed to be zero.
For the actual crossing unit and every integer \(n\),
\[
              e_d(R^\pm)=\kappa^{\pm1}e_d,\qquad
              e_dR^n=\kappa^ne_d .
 \tag{19}
\]
The negative powers are permitted because the original crossing
is a unit. Thus a marked cap propagated only through multiplication
coupons annihilates the wall exactly, including arbitrary fixed
physical powers.

A turn does not preserve this invisible line:
\[
                   Je_d=1,\quad J1=e_d,\qquad
                   \phi\circ J=m,\quad m\circ J=\phi .
 \tag{20}
\]
For example the following literal orders have different wall behavior:
\[
 \begin{split}
 m\circ M_{R^n}\circ J&=\kappa^n\phi,\\
 m\circ J\circ M_{R^n}&=\phi\circ M_{R^n}.
 \end{split}
 \tag{21}
\]
The first has wall norm at most \(4\); the factor has modulus one.
The second uses the full cap vector \(R^n\).
No turn is moved through a multiplication in deriving these formulas.

## 4. A crossing need not preserve the bounded cap estimate

The actual signed crossings have Newton coefficients
\((R^\epsilon)_i=\kappa^\epsilon(-q)^{\epsilon i}\),
\(\epsilon\in\{1,-1\}\). Formula (14) gives
\[
 (W_{R^\epsilon})_{jk}
 =-\kappa^\epsilon(-q)^{\epsilon(d-1)}
       (-q)^{-\epsilon j}(-q)^{-\epsilon k}
       \frac{N^2}{S_{d-1-j-k}^2S_j^2S_k^2}
 \tag{22}
\]
when \(j+k\le d-1\), and zero otherwise.
All its phases factor into a common unit scalar and two unitary
diagonal factors. Hence both signed wall matrices have exactly
the operator norm of the same entrywise nonnegative matrix.
The statement concerns its entries, not positive semidefiniteness.

In fact these norms need not be polynomial in \(N\).
Here is an elementary asymptotic check, requiring no scalar knot
estimate. Put
\[
        J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad0<x<1.
 \tag{23}
\]
For integer \(r_N/N\to x\in(0,1)\),
\[
                    \frac1N\log S_{r_N}\longrightarrow J(x).
 \tag{24}
\]
To justify the improper Riemann sum, subtract \(\log t\).
The remainder is continuous at zero; the sum of \(\log(h/N)\)
converges to its integral by the elementary integral bounds
for \(\log(r!)\), whose error is \(O(\log r)\).
This proves (24). The usual substitution in the sine integral
gives \(J(1/2)=0\). Since \(J'(x)>0\) on \((1/6,1/2)\),
one has \(J(1/3)<0\).

Choose \(j=k=\lfloor(d-1)/3\rfloor\) in (22), so all three
factorial indices divided by \(N\) tend to \(1/3\).
This one matrix entry has rate
\[
 \lim_{N\to\infty}\frac1N
        \log |(W_{R^\epsilon})_{jk}|
                         =-6J(1/3)>0 .
 \tag{25}
\]
The operator norm is at least that entry. Dividing \(R^\epsilon\)
by its norm \(\sqrt N\) does not change this rate.
Thus even a unit-norm actual signed crossing packet can destroy
the bounded-unit-cap conclusion.
This is a statement about a full bilinear wall operator; it is
not a claim about the growth of any selected closed knot scalar.

The exact simplification is therefore to propagate the original
cap first and use its actual direction. A cap in the line
\(\mathbb C e_d\) kills the wall before any estimate. The bare
Frobenius cap has the uniform bound (9). Other directions are
visible by (11), and may require their full coherent estimate.
Disjoint support of the uncontracted bulk and wall tensors does
not alone preserve their orthogonality under these contractions.

## Complete proof sources and scope

Both complete proof sources were read at matching pins:

| Source | SHA-256 |
|---|---|
| [Original centered compiler](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |
| [Shared affine Casimir source](research_centered_tensor_common_casimir_source.md) | df24a9f00dee86aec6ea2c6d7a7861a0b0c050c3c9578885b6db5edf6f590370 |

They supply the original full algebra, signed crossings, exact caps
and turn, positive Newton tensor, and the identified boundary contact.
The wall coefficients, all-cap visibility theorem, word propagation,
and elementary factorial-rate argument are proved above.
Every statement is at the fixed original root and complete main
color; no moving-peripheral or generic-\(q\) jet transport is inferred.
No geometric trial field, arbitrary-short source gap, global
noncancellation theorem or new volume-conjecture class is proved.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or earlier-final edit was performed.
