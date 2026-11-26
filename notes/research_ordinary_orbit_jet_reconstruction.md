# Ordinary-orbit quantum jets reconstruct the complete source

Private written proof, 17 November 2026. Fix the original reduced,
zero-framed knot source. Its complete value at level N is an explicit
linear combination of quantum-normal jets of genuine finite colors
in the noncomplete residue classes modulo N. The maximum normal
order depends only on a fixed braid presentation, and the sum of
the absolute coefficient weights is polynomial in N.

The construction uses an omitted-node Hermite residue row and the
actual integral-color restriction of the same all-root Verma source.
No complete-color value or normal is supplied on the right side.
The resulting row is complex and signed. It gives neither a lower
bound for that row nor a nonzero geometric coefficient.

## 1. Source, normal paths, and a uniform Laurent width

Fix a b-strand braid beta of length ell and writhe w, with one
closed component and zero-framing normalization. Put
\[
 c=b-1-w\in2\mathbb Z,\quad D=N-1,\quad
 q_0=e^{\pi i/N},\quad Q_0=q_0^2,\qquad N\ge2.
                                                               \tag{1}
\]
Let F_N(M) be its actual reduced ADO source in [V]. By [C, (21)]
and the root comparison it is even in M. Write
\[
 F_N(M)=f_N(M^2),\quad Y=M^2,\qquad K_N=f_N(1).
                                                               \tag{2}
\]
The symmetric Alexander polynomial is denoted by Delta, with
Delta(1)=1. All integer colors C_L(q) below are the original
reduced, zero-framed colors, with unknot value one.

Here is a support bound from the literal finite source. The two
canceled checked entries of [V, (1.1)--(1.2)] are
\[
\begin{split}
 R^+_{v+n,u-n;\,u,v}
 &=x^{-u-v+n}Q^{(u-n)v}{u\brack n}_Q
                         (x^{-2}Q^{u-n};Q)_n,\\
 R^-_{v-n,u+n;\,u,v}
 &=x^{u+v-n}Q^{-uv}{v\brack n}_Q
                         (x^2Q^{1-v};Q)_n .
\end{split}                                                    \tag{3}
\]
At the finite root head all input and output indices are between
0 and D. In the positive entry n<=u, and its x powers are
\(-u-v+n-2h\), 0<=h<=n, lying in [-3D,0].
In the negative entry n<=v, and its powers
\(u+v-n+2h\) lie in [0,3D]. The Gaussian coefficients
and root chirps have no x dependence.

The finite head numerator P in [V, Section 3] retains the scalar
x^c. Its exact ordinary-pivot to ADO-pivot comparison is
\[
 P_{N,\beta}(x;1)=x^{Nc}F_N(-q_0x).                \tag{4}
\]
Consequently F_N(-q0 x), rather than P itself, retains the
overall power \(x^{-(N-1)c}\). Every exponent of this actual
reduced source therefore has absolute value at most
\((3\ell+|c|)(N-1)\). Evenness and the marked substitution
\(x=-q_0^{-1}M\) give
\[
 \operatorname{supp} f_N\subset[-AN,AN],\qquad
 A=\max\!\left(1,\left\lceil\frac{3\ell+|c|}{2}\right\rceil\right).
                                                               \tag{5}
\]
The support interval is deliberately generous and valid at every
N>=2. No degree estimate for a different knot invariant is used.

The full ADO normalization, if required, is still exactly
\[
 \mathcal N_N(M)
   =i^{N+3}\frac{M^{N-1}}{S_N(M^2)}f_N(M^2),\qquad
 S_N(Y)=1+Y+\cdots+Y^{N-1}.                       \tag{6}
\]
Our target is the reduced complete value (2). Neither the phase,
the monomial in (6), nor the distinction between the full and
reduced sources is absorbed into an unspecified scalar.

## 2. The omitted-complete-node residue row

Fix once and for all
\[
                         H=4A+1.                \tag{7}
\]
Then \(H(N-1)>2AN\) for every N>=2. Define
\[
 \omega_N(Y)=
 \frac{Y^{AN}f_N(Y)}{(Y-1)S_N(Y)^H}\,dY
 =\frac{Y^{AN}(Y-1)^{H-1}f_N(Y)}
        {(Y^N-1)^H}\,dY.                        \tag{8}
\]
The factor Y^{AN} clears all Laurent powers. Its numerator in the
first expression has degree at most 2AN, whereas the denominator
has degree \(1+H(N-1)\ge2AN+2\). Thus (8) has no pole at zero and
has zero residue at infinity. Its residue at Y=1 is K_N/N^H.
Every other pole lies at
\(\zeta_L=Q_0^L\), \(1\le L<N\), and has order at most H.
The residue theorem proves the exact source identity
\[
 K_N=-N^H\sum_{L=1}^{N-1}
                         \operatorname{Res}_{Y=\zeta_L}\omega_N.
                                                               \tag{9}
\]
Only the ordinary nodes occur on the right side.

We make every coefficient in this Hermite row explicit. Set
\[
 \mathscr E_N=\frac1N Y\partial_Y,\qquad
 \Psi_{A,H,N}(t;\zeta)=
 e^{At}\zeta e^{t/N}(\zeta e^{t/N}-1)^{H-1}
                   \left(\frac{t}{e^t-1}\right)^H,\qquad
 b_{h,N}(\zeta)=[t^h]\Psi_{A,H,N}(t;\zeta).
                                                               \tag{10}
\]
The removable value at t=0 is retained. In the local coordinate
\(Y=\zeta e^{t/N}\) one has \(\zeta^{AN}=1\), \(Y^N=e^t\), and
\[
 \omega_N=\frac1N t^{-H}\Psi_{A,H,N}(t;\zeta)
                              f_N(\zeta e^{t/N})\,dt .
\]
Expanding the last factor by its actual Euler derivatives gives
\[
 K_N=-N^{H-1}\sum_{L=1}^{N-1}\sum_{a=0}^{H-1}
   \frac{b_{H-1-a,N}(\zeta_L)}{a!}
                          (\mathscr E_N^a f_N)(\zeta_L).
                                                               \tag{11}
\]
This formula includes all normals through H-1.

There is a uniform coefficient bound with no root-spacing loss.
For |t|=1,
\[
 \left|\frac{e^t-1}{t}-1\right|
       \le\sum_{j=2}^\infty\frac1{j!}=e-2<1.
\]
The last strict inequality follows, for example, by bounding the
factorial tail geometrically. Cauchy's coefficient estimate gives
\[
 |b_{h,N}(\zeta)|\le B_{A,H}:=
 e^{A+1/2}(1+e^{1/2})^{H-1}(3-e)^{-H},
 \quad |\zeta|=1,\quad N\ge2,\quad h\ge0.          \tag{12}
\]
Thus the total absolute row weight in (11) is at most
\(eB_{A,H}N^H\). In ordinary derivative coordinates, the coefficient
of \(f_N^{(r)}(\zeta_L)\) is \(O_{A,H}(N^{H-1-r})\).
Indeed induction gives
\((Y\partial_Y)^a=\sum_{r=0}^a s_{a,r}Y^r\partial_Y^r\)
with fixed integer coefficients; only a>=r contributes and
each term in (11) contains N^{-a}. This also shows directly why
nearby ordinary nodes cause no inverse-distance blowup in this row.

## 3. The exact high-color quantum-normal adapter

Use the fixed root-normal coordinate
\[
 \delta=1-q^{2N},\qquad
 q(\delta)=q_0(1-\delta)^{1/(2N)}.                 \tag{13}
\]
The formal fixed-Y completion proved in [C, (25a)--(26)] satisfies
\[
 \mathcal W_N(\delta,Y)=\sum_{j\ge0}\delta^j W_{j,N}(Y),
 \qquad W_{0,N}(Y)=g_N(Y):=\frac{f_N(Y)}{\Delta(Y^N)}.
                                                               \tag{14}
\]
Its coefficients are rational in Y, with poles only at zero,
infinity, and the Alexander divisor. They are regular at every
\(\zeta_L\). This statement concerns the specified formal
completion, not an assumed convergent quantum series.

For \(1\le L<N\), h>=0 and r>=0 put
\[
 J_{h,L,N}(r)=[\delta^h]C_{L+rN}(q(\delta)).        \tag{15}
\]
The ANY-positive-color quotient in [C, Section 6] retains every
intermediate index and the ordinary pivot before root restriction.
Together with the natural meridian \(Y=q^2x^2\), it gives exactly
\[
 C_{L+rN}(q(\delta))
  =\mathcal W_N\!\left(
       \delta,\zeta_L(1-\delta)^{r+L/N}\right).
                                                               \tag{16}
\]
The equality is one of formal delta germs. Its evaluation of the
auxiliary grading at one is legitimate: at the corresponding root
x=q0^{L-1} up to sign, the deleted classical compression is
nilpotent, so its determinant is identically one in the grading,
as proved in [C, (23)]. There is no independently frozen root pivot
or identification of fixed-Y normals with integral-color normals.

Let \(E=Y\partial_Y\) and \(\eta=\log(1-\delta)\).
Expanding the right side of (16) yields
\[
 \sum_{a,d\ge0}\delta^a
       \frac{(r+L/N)^d\eta^d}{d!}
                         (E^dW_{a,N})(\zeta_L).   \tag{17}
\]
At order h only a+d<=h occurs. Hence J_{h,L,N}(r)
is a polynomial in r of degree at most h, for every r>=0.
Its leading coefficient is
\((-1)^h(E^h g_N)(\zeta_L)/h!\).
The elementary h-th finite difference therefore gives
\[
 B_{h,L,N}:=\sum_{r=0}^h(-1)^r\binom hr J_{h,L,N}(r)
                      =(E^h g_N)(\zeta_L).       \tag{18}
\]
For h=0 this is the original ordinary-color value. The sign in
(18) includes the leading coefficient of log(1-delta); no parity
character remains in the squared-meridian coordinate.

Retain the entire Alexander factor by defining
\[
 \alpha_s=\left.(Z\partial_Z)^s\Delta(Z)\right|_{Z=1},
 \qquad \alpha_0=1.
\]
Since \(\zeta_L^N=1\), the ordinary product rule gives exactly
\[
 (\mathscr E_N^a f_N)(\zeta_L)
   =\sum_{h=0}^a\binom ah N^{-h}\alpha_{a-h}B_{h,L,N}.
                                                               \tag{19}
\]
In particular neither the denominator in (14) nor its higher
normal derivatives have been replaced just by Delta(1).

## 4. Explicit reconstruction from genuine finite-color jets

Combining (11), (18), and (19) proves
\[
 K_N=\sum_{L=1}^{N-1}\sum_{h=0}^{H-1}\sum_{r=0}^h
                         w_{L,h,r,N}J_{h,L,N}(r), \tag{20}
\]
where every weight is specified by
\[
 w_{L,h,r,N}
  =-(-1)^r\binom hr N^{H-1-h}
       \sum_{a=h}^{H-1}
        \frac{b_{H-1-a,N}(\zeta_L)}{a!}
                              \binom ah\alpha_{a-h}.
                                                               \tag{21}
\]
The source quantities on the right use only the colors
\[
 1\le L<N,\qquad 0\le r\le h\le H-1,\qquad
                           L+rN\le HN-1.         \tag{22}
\]
No color is divisible by N. In particular no complete-color value
or quantum normal is input to this reconstruction. For r>=1,
these are genuine high colors in ordinary residue classes; they
are not the bounded ordinary colors strictly below N.

All row weights are polynomially controlled. Put
\[
 A_{\Delta,H}=\sum_{s=0}^{H-1}\frac{|\alpha_s|}{s!}.
\]
Using \(\binom ah/a!=1/(h!(a-h)!)\), (12) gives
\[
 |w_{L,h,r,N}|
 \le B_{A,H}A_{\Delta,H}\frac{\binom hr}{h!}
                                           N^{H-1-h},
                                                               \tag{23}
\]
and consequently
\[
\begin{split}
 \sum_{L=1}^{N-1}\sum_{r=0}^h |w_{L,h,r,N}|
 &\le B_{A,H}A_{\Delta,H}\frac{2^h}{h!}N^{H-h},\\
 \sum_{L,h,r}|w_{L,h,r,N}|
 &\le e^2B_{A,H}A_{\Delta,H}N^H.                 \tag{24}
\end{split}
\]
The maximum derivative order H-1 is fixed with the presentation.
The coefficient bounds hold at every N>=2 and for all its ordinary
residue classes, without primality assumptions.

Equations (20)--(24) are an exact original-source reconstruction
with an explicit polynomially bounded row. They do not claim a
polynomially conditioned inverse for all the supplied data, which
contain redundancy, or a positive representation of the scalar.

## 5. What the existing positive norm does and does not provide

For comparison, [P, Sections 1--3] already proves
\[
 f_N(\zeta_L)=C_L(q_0),\qquad
 |C_L(q_0)|\le D_N:=\sin(\pi/N)^{1-b}
                      \le(N/2)^{b-1},\quad 1\le L<N.            \tag{25}
\]
Its exact positive cyclic norm is
\[
 \mathcal H_N=\frac1N\sum_{Y^N=1}|f_N(Y)|^2
     =\frac{|K_N|^2}{N}
           +\frac1N\sum_{L=1}^{N-1}|C_L(q_0)|^2. \tag{26}
\]
Thus a positive exponential estimate for that specified norm would
control K_N, but such an estimate is not supplied by positivity.

The h=0 portion of (20) has a polynomial bound by (24)--(25).
Higher h involve the actual normal data (15). The ordinary-color
positive trace bounds do not bound these transverse quantum jets
or the high colors with r>=1. In particular (20) alone cannot
turn those positive bounds into a lower bound for K_N: its weights
are signed and complex, and the identities retain cancellation.
The all-root coefficient upper estimates are also not a lower
bound for this selected row. No analytic summation theorem is used
in (16)--(20), because fixed-order restrictions are exact formal
identities of the genuine finite sources.

## 6. Coverage, scope, and complete proof sources

[P] already contains ordinary-node interpolation with S_N to the
first power, the regular quotient, actual ordinary-color bounds,
and the positive Fourier norm (26). Full-orbit Fourier/Hermite
sampling and bounded meridian jets have also been studied in the
existing notes. The present calculation specifically omits the
complete node, chooses a fixed higher S_N power from the literal
Laurent width, and replaces every required meridian normal by the
finite differences of actual quantum-normal data in (18).

Derivative recovery of nonsemisimple knot invariants and recovery
of ADO data from the colored-Jones family have literature coverage:
[Murakami, arXiv:1406.1287](https://arxiv.org/abs/1406.1287) states
a derivative relation for logarithmic invariants, and
[Willetts, arXiv:2003.09854](https://arxiv.org/abs/2003.09854) states
a unification determining root ADO data from the colored family.
These are statement-level coverage only, not proof premises.
No broad novelty is asserted for derivative recovery or Hermite
interpolation.

The complete proof directs are:

| Label | Complete source | SHA256 |
|---|---|---|
| V | notes/frobenius_verma_period.md | b11489368e7ac1106c7a5e760154b0713dfbc7eaf9b76193438df57b48041a90 |
| C | notes/research_all_root_verma_normal_rationality.md | 46e984e3ce5491ff82a18da6914d89a0e42393fd7e66877dc679190e69b125f6 |
| P | notes/regularized_kashaev_period.md | d7efc1e6e2995a0bff7553553e044f8554e559e51cdf8515d8048e2f603b94fc |

V supplies the literal entries, finite head source, and exact
pivot/framing normalization (3)--(6). C supplies evenness, the
canonical natural-meridian completion and its actual integral-color
restrictions, including regularity at every ordinary orbit point.
P supplies only the original ordinary-color identities and bounds
and the positive-norm comparison in Section 5. The Laurent width,
omitted-node residue, explicit coefficients, finite-difference
adapter, and weight bounds are proved above by written arguments.
No mathematical programs, tests, or numerical cases are used.

