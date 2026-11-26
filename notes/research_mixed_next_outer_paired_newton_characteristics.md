# Paired finite Newton recurrences and their principal trace surface

Private exact-source deduction, 8 November 2026. The remaining
physical middle sum has two finite recurrences: the original
adjoint relation for its inner periods and a centered three-term
equation for its retained outgoing coefficients. Both forcings
and the finite summation-by-parts endpoints are retained below.

Their principal characteristics give an explicit prospective
resultant on a Fricke trace surface. We prove its degree and
nonzero leading coefficient, but not its nonvanishing at an
actual outgoing reference. No marked peripheral-polynomial
identification, inverse estimate, or suppression of the middle
sum is asserted. No mathematical numerical evaluation is used.

## 1. The two actual coefficient sequences

Use
\[
\begin{gathered}
N\ge6,\quad D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
\kappa=q^{D^2/2},\\
M=\lceil N/2\rceil,\quad U=\lfloor N/2\rfloor-1,\quad
L=\lfloor N/6\rfloor,\quad K=\lfloor N/4096\rfloor,\\
P_k=(r;r)_k,\qquad p_k(Z)=(rZ;r)_k,\qquad Y_b=r^b .
\end{gathered}                                                     \tag{1}
\]
Use the original Newton normalization
\[
c_j=2\cos((2j+1)\pi/N),\quad
s_j=2\sin(\pi j/N),\quad S_j=\prod_{\nu=1}^j s_\nu,\quad
e_b(w)=S_b^{-2}\prod_{j<b}(c_j-w),\quad S_0=1.
\]
The original physical rows and their retained sum are
\[
R_{b,k}(Z)=\frac{Y_b^{-k}p_k(Y_b)p_k(Z)}{P_k^2},\qquad
C_b^{>}(Z)=\sum_{k=K+1}^{D}R_{b,k}(Z).
                                                                    \tag{2}
\]
At \(1\le b\le D\), each row with \(k>D-b\) is zero, so
(2) is exactly the original terminating sum. No negative
factorial is introduced beyond that stop.

Keep the complete inner output and the original periods
\[
\lambda_{b,N}=\phi_N(R^3e_bQ_N^{\rm full}),\qquad
\sigma_{b,N}=\phi_N(R^3e_b),\qquad
a_{b,N}(Z)=(-q)^b C_b^{>}(Z).
                                                                    \tag{3}
\]
For \(M\le b\le D-L\), \(\lambda_{b,N}\) is precisely the
original high Newton coefficient \(\ell_b(-2)\). Thus
[the exact Newton source identity, equation (16)](research_mixed_next_middle_exact_newton_coefficients.md)
writes the remaining observation as
\[
\frac1{\kappa^2N}
       \sum_{b=M}^{D-L}a_{b,N}(Z_*)\lambda_{b,N}.
                                                                    \tag{4}
\]
There is no extra \(+N\), omitted radical normal, or changed
Fourier sector in (4).
Its actual-reference application retains complete words in
powers three and four beginning \(343\), of length at least
five, with the original outside values \(w=-2\), \(Z=Z_*\).

## 2. The exact outgoing recurrence and its retained cutoff forcing

Define
\[
A_b=Y_b(Y_b-1),\qquad
B_b=3Y_b-(1+r)Y_b^2,\qquad
C_b=r^{-1}(1-rY_b)^2.
                                                                    \tag{5}
\]
The letter \(C_b\) without a superscript in (5) is an
operator coefficient; the outgoing sum is \(C_b^{>}\).

**Proposition 1.** For \(1\le b\le D-1\),
\[
\boxed{\quad
Z C_b^{>}
 =A_bC_{b-1}^{>}+B_bC_b^{>}+C_bC_{b+1}^{>}
    +r^{-K-1}(1-r^{K+1}Z)R_{b,K}(Z).
\quad}                                                            \tag{6}
\]
All terms are ordinary polynomials in \(Z\), with the original
physical specializations in their first variable. The complete
sum starting at \(k=0\) satisfies the same equation with zero
forcing.

*Proof.* Use the exact ordered operator and telescoping identity
of [the conditional difference theorem, equations (5), (10c),
and (10d)](research_mixed_three_fourier_conditional_difference_equation.md).
Write its incoming argument as \(X=Y_b/r\). At this point
\[
\mathsf DF=(1-Y_b)F(rX)+Y_bF(X),
\]
and
\[
\mathsf D^2F
 =(1-Y_b)(1-rY_b)F(r^2X)
   +Y_b(1-Y_b)(1+r)F(rX)+Y_b^2F(X).
                                                                    \tag{7}
\]
Substitution into that original operator gives exactly
\[
\mathcal L_{N,Z}F(Y_b/r)
 =\frac{1-Y_b}{Y_b}
       \{ZF(Y_b)-A_bF(Y_b/r)-B_bF(Y_b)-C_bF(rY_b)\}.
                                                                    \tag{8}
\]
The coefficients are not commuted past a shift in this calculation.

For the sum over \(k=K+1,\ldots,D\), the source telescopes
to its lower-cut term
\[
(r^{-K-1}-1)^2R_{b-1,K+1}(Z).
                                                                    \tag{9}
\]
The original upper term is
\((1-Z^N)(X^{-N}-1)/N^2\), and is zero at this physical
\(X=r^{b-1}\). It is removed only after that exact
specialization. In particular there is no denominator \(P_N\).

The finite product recurrence gives the undivided identity
\[
(r^{-K-1}-1)^2R_{b-1,K+1}(Z)
 =\frac{1-Y_b}{Y_b}\,
        r^{-K-1}(1-r^{K+1}Z)R_{b,K}(Z).
                                                                    \tag{10}
\]
For example, use
\(p_{K+1}(Y_b/r)=(1-Y_b)p_K(Y_b)\) and
\(P_{K+1}=(1-r^{K+1})P_K\).
This proof divides by no outgoing numerator; (10) holds
through all numerator zeros and all terminating rows.
Since \(Y_b\ne1\) in the stated range, (8)--(10) prove (6).
For the complete sum the original lower boundary is zero
as well, proving its homogeneous statement. \(\square\)

After the exact sign normalization in (3), put
\[
f_{b,N}(Z)=(-q)^b r^{-K-1}
                         (1-r^{K+1}Z)R_{b,K}(Z).
                                                                    \tag{11}
\]
Then (6) becomes
\[
Za_b=(\mathcal J_Na)_b+f_{b,N},\qquad
(\mathcal J_Na)_b=-qA_ba_{b-1}+B_ba_b-q^{-1}C_ba_{b+1}.
                                                                    \tag{12}
\]
The factors \(-q\) and \(-q^{-1}\) have not been replaced
by an unsigned conditional recurrence.

At the actual \(|Z_*|<8/7\), the forcing in (11), in its
literal original pairing, is already an eligible single
small-outgoing row. Specifically, for every subset
\(\mathcal I_N\subseteq\{M,\ldots,D-L\}\),
[the small-outgoing-index theorem](research_mixed_next_three_small_outgoing_indices.md)
gives
\[
\left|\frac1{\kappa^2N}
      \sum_{b\in\mathcal I_N}\lambda_{b,N}f_{b,N}(Z_*)\right|
 \le C N^A
       e^{N(419/200-3/1000)}.
                                                                    \tag{13}
\]
Indeed take precisely its row \(k=K\); an already terminated
row contributes zero. The extra common factor
\(r^{-K-1}(1-r^{K+1}Z_*)\) has modulus at most \(15/7\).
Equation (13) does not estimate a later forcing multiplied
by unbounded or unestimated elimination coefficients.

## 3. The exact period relation and both finite endpoints

Use the ordinary operator and Newton coefficients of
[the finite-remainder theorem, equations (2), (17)](research_mixed_next_outer_finite_newton_remainder.md):
\[
\begin{split}
\mathcal B_N
 &=q^{-2}\mathcal L_2(\mathcal L_3^2-I)
       +q^{-3}Z_{\rm sp}\mathcal L_3-8q^{-2}\mathcal L_3
                                  +(8q^{-1}+2)I,\\
\mathcal B_Ne_b
 &=\sum_{\nu=-3}^{8}b_{b,\nu,N}e_{b+\nu},\qquad
b_{b,8,N}=q^{27+6b}\frac{S_{b+8}^2}{S_b^2}.
\end{split}                                                       \tag{14}
\]
Here \(Z_{\rm sp}\) means multiplication by the spectral
polynomial variable, not the outgoing parameter in (2).
For
\[
                       M+3\le b\le D-L-8,
                                                                    \tag{15}
\]
all terms stay in the actual radical band. Full adjoint
pairing, with the original seven-term equation, gives
\[
\boxed{\quad
\sum_{\nu=-3}^{8}b_{b,\nu,N}\lambda_{b+\nu,N}
                       =\mathfrak f_N\sigma_{b,N},
\qquad
\mathfrak f_N=
\begin{cases}
4\kappa^3/N^2,&N\text{ even},\\
0,&N\text{ odd}.
\end{cases}
\quad}                                                            \tag{16}
\]
No new endpoint normal occurs in (16). It follows from the
full polynomial relation, with the three test zeros built
into \(e_b/e_M\) on (15).

The [original radical contraction, Theorem 2](research_high_newton_radical_contraction.md)
also gives, for every \(M\le b\le D\),
\[
|\sigma_{b,N}|\le2(D-b+1)\le N,\qquad
|\mathfrak f_N\sigma_{b,N}|\le4/N
                         \quad(N\text{ even}).
                                                                    \tag{17}
\]
The odd forcing is exactly zero. These bounds do not estimate
the period \(\lambda_{b,N}\).

The bilinear transpose of the signed outgoing operator is
\[
(\mathcal J_N^{\mathrm t}\lambda)_b
       =-qA_{b+1}\lambda_{b+1}
              +B_b\lambda_b-q^{-1}C_{b-1}\lambda_{b-1}.
                                                                    \tag{18}
\]
For any integer interval \([\alpha,\beta]\) contained in
(15), its exact finite identity is
\[
\begin{split}
Z\sum_{b=\alpha}^{\beta}a_b\lambda_b
 -\sum_{b=\alpha}^{\beta}a_b
                         (\mathcal J_N^{\mathrm t}\lambda)_b
 =\sum_{b=\alpha}^{\beta}\lambda_b f_{b,N}
                         +\mathcal E_{\alpha,\beta},
\end{split}                                                       \tag{19}
\]
where all four endpoint terms are
\[
\begin{split}
\mathcal E_{\alpha,\beta}={}&
 -qA_\alpha\lambda_\alpha a_{\alpha-1}
 -q^{-1}C_\beta\lambda_\beta a_{\beta+1}\\
 &+q^{-1}C_{\alpha-1}a_\alpha\lambda_{\alpha-1}
 +qA_{\beta+1}a_\beta\lambda_{\beta+1}.
\end{split}                                                       \tag{20}
\]
Direct reindexing proves (19)--(20). In particular no zero
extension is imposed on either original coefficient sequence.
Equations (12),(16),(19) are the exact finite relations
available before any proposed Bezout construction.

## 4. Principal characteristics with the original sign

Let \(b/N\) tend to a fixed point of the physical middle
interval, and write
\[
x=e^{2\pi ib/N},\qquad
\mathfrak s=2-x-x^{-1},\qquad
z\ \text{for the period shift }\lambda_{b+1}/\lambda_b.
                                                                    \tag{21}
\]
This notation defines a principal Laurent symbol, not an
assertion that an actual period has that ratio.
The physical middle arc is
\[
\mathcal X=\{e^{2\pi i t}:1/2\le t\le5/6\};
\qquad x\ne0,1\ \text{on }\mathcal X.
                                                                    \tag{22}
\]
Finite shifts of \(b\) change its coefficients by \(O(N^{-1})\)
on a fixed neighborhood of this arc. This follows directly
from the explicit trigonometric Newton coefficients, and
licenses their commuting leading symbols.

The three symbols obtained from the original Newton actions
of \(Z_{\rm sp},\mathcal L,\mathcal L_1\) are
\[
\begin{split}
\mathsf X&=2-\mathfrak s(1+z),\\
\mathsf Y&=2-\mathfrak s(1+z^{-1}),\\
\mathsf V&=x\mathfrak s(z+z^{-1})+4x-2x^2
             =2-(x-1)^2\frac{(z+1)^2}{z}.
\end{split}                                                       \tag{23}
\]
For example the last formula retains the two original
\(q^{2b}\) shift coefficients of \(\mathcal L_1e_b\);
the diagonal tends to \(4x-2x^2\).
Define
\[
V_0=\mathsf Y,\quad V_1=\mathsf V,\qquad
V_{n+1}=8-\mathsf X V_n-V_{n-1}.
                                                                    \tag{24}
\]
Then the actual period operator in (14) has principal symbol
\[
\boxed{\quad
\mathfrak b(x,z)
       =(V_3^2-1)V_2+(\mathsf X-8)V_3+10 .
\quad}                                                            \tag{25}
\]
This is a Laurent polynomial with shifts from \(-3\) through
eight, exactly matching the original finite band.

The principal symbol needed from the outgoing equation is
that of its *signed transpose* (18). Since \(Y_b\to x^{-1}\),
it is
\[
\mathfrak j^{\mathrm t}(x,z)
 =\frac{3x-2+(x-1)z-(x-1)^2z^{-1}}{x^2}.
                                                                    \tag{26}
\]
Thus a common root relevant to a prospective local operator
elimination must satisfy
\[
\mathfrak b(x,z)=0,\qquad
\mathsf Q(x,z,Z):=
(x-1)z^2+(3x-2-x^2Z)z-(x-1)^2=0.
                                                                    \tag{27}
\]
Using the unsigned outgoing shift, or not transposing it,
would give a different common-root equation. No forcing in
(12) or (16) has been removed by stating their symbols.

## 5. The trace surface and a nontrivial prospective resultant

The parametrization (23) satisfies exactly
\[
\boxed{\quad
(\mathsf X+\mathsf Y+\mathsf V-6)^2
       +(\mathsf X-2)(\mathsf Y-2)(\mathsf V-2)=0.
\quad}                                                            \tag{28}
\]
To verify it, put \(d=x-1\). The three shifted quantities are
\[
\mathsf X-2=\frac{d^2(z+1)}x,\qquad
\mathsf Y-2=\frac{d^2(z+1)}{xz},\qquad
\mathsf V-2=-\frac{d^2(z+1)^2}z .
                                                                    \tag{29}
\]
Their sum is \(-d^3(z+1)^2/(xz)\), whose square is the
negative of their product. This proves (28).
It is the Fricke trace-surface identity in these coordinates;
no marked topological identification is inferred from it.

The denominator and Laurent powers in (25) are cleared by
\[
\mathsf P(x,z)=x^5z^3\mathfrak b(x,z)\in\mathbb C[x,z].
                                                                    \tag{30}
\]
Indeed \(V_2\) has \(x\)-denominator at most one, and \(V_3\)
at most two, so their product in (25) has denominator at most
five. The extreme \(z\)-coefficients can be read without
expanding the full polynomial:
\[
[z^{11}]\mathsf P=(x-1)^{16},\qquad
\mathsf P(x,0)=x^{10}(x-1)^6.
                                                                    \tag{31}
\]
For the first, the leading positive powers of
\(\mathsf X,V_1,V_2,V_3\) are respectively
\(-\mathfrak s z,\ x\mathfrak s z,\
x\mathfrak s^2z^2,\ x\mathfrak s^3z^3\).
Thus the top term of \(\mathfrak b\) is
\(x^3\mathfrak s^8z^8=(x-1)^{16}x^{-5}z^8\).
At \(z=0\), the lowest powers of \(V_2,V_3\) are
\(-x^2\mathfrak s z^{-1}\) and
\(x^3\mathfrak s z^{-1}\). Their contribution is
\(-x^8\mathfrak s^3z^{-3}=x^5(x-1)^6z^{-3}\).
This proves the constant term after (30).

In particular, for \(x\in\mathcal X\), \(\mathsf P\) has
degree eleven and no zero root, while \(\mathsf Q\) has
degree two and no zero root. Define the prospective resultant
with the order of its arguments fixed:
\[
\mathsf R(x,Z)=\operatorname{Res}_z
                              (\mathsf P(x,z),\mathsf Q(x,z,Z)).
                                                                    \tag{32}
\]
It vanishes exactly when the two principal polynomials have
a common finite root. As a polynomial in \(Z\), it has
degree eleven with
\[
\boxed{\qquad
[Z^{11}]\mathsf R(x,Z)=x^{32}(x-1)^{22}.
\qquad}                                                           \tag{33}
\]
For example, if \(z_1,\ldots,z_{11}\) are the roots of
\(\mathsf P(x,\cdot)\), counted with multiplicity, the
product formula for the resultant gives its leading term
as
\[
(\operatorname{lc}_z\mathsf P)^2\,(-x^2)^{11}
                    \prod_{\nu=1}^{11}z_\nu
 =x^{22}\mathsf P(x,0)[z^{11}]\mathsf P,
\]
where \(\operatorname{lc}_z\) denotes the leading coefficient.
Substitution of (31) proves (33). This
argument also applies to multiple roots by the same polynomial
identity.

Thus the resultant is not identically zero in \(Z\) at any
point of the physical middle arc. This does **not** prove
\(\mathsf R(x,Z_*)\ne0\) for the actual reference, or give a
uniform lower bound there. Neither does a pointwise principal
Bezout identity automatically control an exact finite operator
inverse, its accumulated shifts, the retained forcings, or
the four terms (20).

The finite-remainder theorem therefore still has its eleven
correlated observations and unestimated elimination cost.
Equations (12),(16),(27)--(33) identify an exact-source route
for investigating those correlations. They do not turn a
generic trace-surface relation into the marked gluing
equations or a peripheral polynomial of the original knot.
