# Complex zeros of the actual pure-source Fourier polynomial

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged. This consolidates and strengthens the separate
finite-window calculation without editing its frozen text.

The even color Fourier polynomial of an actual strict Conway source
need not be real stable or Lee–Yang zero-free. The complete source of
one strict two-circle construction has a simple explanation: its
diagonal is a sum of real squares containing the constant \(N^4\).
It is a nonconstant polynomial, so every diagonal zero is nonreal.
The associated fugacity zeros occur in every combination of the unit
disk and its exterior.

All statements concern the specified finite color window. Every wire,
signed alias and Casimir normal is retained in the complete-source
theorem. The positive wire corridor used in the filling proof has a
separate version proved at the end. Neither version locates a zero
relative to a short filling's geometric saddle.

## 1. The strict construction and its physical samples

Fix \(N\ge3\), and set
\[
 d=N-1,\qquad M=\lfloor d/2\rfloor,\qquad
 q=e^{\pi i/N},\qquad \theta=\pi/N,\qquad
 S_j=\prod_{k=1}^j2\sin(k\theta),\quad S_0=1.
 \tag{1}
\]
Let \(e_0,\ldots,e_d\) be the normalized Newton basis of the full
pair Casimir algebra. The genuine physical quarter-turn \(\mathcal T\)
and original marked Frobenius closing \(\phi\) satisfy
\[
 \mathcal T e_j=e_{d-j},\qquad
 \phi(e_i e_j)=\delta_{i+j,d},\qquad
 \phi(f\mathcal T g)=\sum_{r=0}^d f_rg_r .
 \tag{2}
\]
These are full polynomial identities, including repeated-root
directions. The last pairing is bilinear.

Take two distinct elementary boxes and the construction
\[
                         \tau=C\bigl(h_1\,\mathcal T(h_2)\bigr).
 \tag{3}
\]
It is strict: give each leaf coordinate \(1/4\), so the closing
outputs are \(1/4,3/4\). There is no retained product below that
root. Equivalently its closing types are \(L,H\). With no retained
half twists, the main-strand pairings are \(U,I\); their stack is
\(U\), no internal circle occurs, and cylindrical closure gives
one main component. Thus (3) is an admissible strict construction,
not a manufactured coefficient array. This does not assert that a
particular short filling is hyperbolic.

For an ordinary auxiliary color \(j\), let \(L_j\) be the original
circle with its original pivot and put
\(\mathsf h_j=\mathcal T(L_j)\), with no extra half twist. Write
\[
                 \mathsf h_{N-a}=\sum_{r=0}^d a_{r,N}(a)e_r
                       \qquad(0\le a\le M).
 \tag{4}
\]
The exact pure-leaf identity is
\[
 \mathsf h_{N-a}
  =\sum_{r=a}^M A_{N,r}(a)e_r+(-1)^N\mathsf h_a,\qquad
 A_{N,r}(a)=
       \frac{N^2S_{2r}}{S_r^2S_{r-a}S_{r+a}}>0 .
 \tag{5}
\]
Here \(\mathsf h_0=0\). For \(a>0\), the alias \(\mathsf h_a\)
has real coefficients and support in indices at least \(N-a>M\).
Every coefficient in (4) is therefore real. In particular,
\[
 \boxed{\quad
 a_{0,N}(0)=N^2,\quad a_{0,N}(a)=0\ (1\le a\le M),\qquad
 a_{r,N}(a)=A_{N,r}(a)\ (a\le r\le M).
 \quad}
 \tag{6}
\]
The complete original physical samples for (3) are
\[
 \mathcal A_N(a,b)
   =\phi\bigl(\mathsf h_{N-a}\,
                        \mathcal T(\mathsf h_{N-b})\bigr)
   =\sum_{r=0}^d a_{r,N}(a)a_{r,N}(b).
 \tag{7}
\]
No alias or normal has been removed. Equation (7) uses the original
source normalization; a separately recorded common framing unit
would not change any zero below.

## 2. A constant feature forces nonreal zeros

Choose any integer window
\[
                              1\le H\le M .
 \tag{8}
\]
Apply the prescribed even Fourier operation only on that window:
\[
 \mathscr F_{N,H}(z_1,z_2)
   =\sum_{a,b=-H}^H
            \mathcal A_N(|a|,|b|)z_1^az_2^b .
 \tag{9}
\]
Only the actual colors \(N,N-1,\ldots,N-H\) have been sampled.
There is no assertion about an untruncated color orbit. In particular,
a sufficiently small cutoff \(H=\lfloor\delta N\rfloor\) in the
filling argument lies in (8) at all sufficiently large levels.

Define real polynomials
\[
 p_r(u)=a_{r,N}(0)+2\sum_{a=1}^H a_{r,N}(a)T_a(u/2),
 \qquad
 K_{N,H}(u,v)=\sum_{r=0}^d p_r(u)p_r(v).
 \tag{10}
\]
Here \(T_a\) is the ordinary Chebyshev polynomial. Its identity
\(2T_a((z+z^{-1})/2)=z^a+z^{-a}\) and (7) give exactly
\[
 \mathscr F_{N,H}(z_1,z_2)
       =K_{N,H}(z_1+z_1^{-1},z_2+z_2^{-1}).
 \tag{11}
\]
All \(d+1\) features remain. Equation (6) gives
\[
                             p_0(u)=N^2 .
 \tag{12}
\]
Also \(p_M\) has degree \(H\), since its leading coefficient is
\(a_{M,N}(H)=A_{N,M}(H)>0\). Every other feature has degree at
most \(H\). Consequently the real diagonal polynomial
\[
                         D_{N,H}(u)=K_{N,H}(u,u)
 \tag{13}
\]
has degree \(2H\): the squares of its real leading coefficients
cannot cancel. On the entire real line it satisfies
\[
                            D_{N,H}(u)\ge N^4 .
 \tag{14}
\]
It therefore has \(2H\) zeros counted with multiplicity and none
is real. Its real coefficients give at least one zero \(u_0\) in
the upper half-plane.

A real polynomial in two variables is real stable if it is nonzero
whenever both variables have positive imaginary part. Since
\(K_{N,H}(u_0,u_0)=0\), the actual full-source polynomial
\(K_{N,H}\) is not real stable for every \(N,H\) in (8).
This argument uses the protected constant feature directly; it needs
no general preservation theorem for stable polynomials.

## 3. Zeros in every disk/exterior choice

Clear the Laurent powers by
\[
          P_{N,H}(z_1,z_2)
                =(z_1z_2)^H\mathscr F_{N,H}(z_1,z_2).
 \tag{15}
\]
This is an ordinary polynomial. The solutions of
\(z^2-u_0z+1=0\) are nonzero and cannot lie on the unit circle,
because \(z+z^{-1}\) is real there. Their product is one, so
they can be labeled \(z_-,z_+=z_-^{-1}\), with
\(0<|z_-|<1<|z_+|\). Equation (11) gives
\[
                P_{N,H}(z_\varepsilon,z_\delta)=0
                        \qquad(\varepsilon,\delta\in\{-,+\}).
 \tag{16}
\]
The monomial in (15) is nonzero at these points. Thus the actual
finite-window polynomial fails all four nonvanishing conditions
obtained by choosing the open unit disk or its exterior independently
for the two fugacities. In particular it has no standard
disk/exterior Lee–Yang property. Independent reversal of the fugacity
orientations does not help: the Laurent polynomial is separately
reciprocal, and (16) already covers all four choices.

## 4. The Gaussian factor does not supply positive definiteness

For the same complete source set
\[
                  A(t)=\mathscr F_{N,H}(e^{2\pi it},1).
 \tag{17}
\]
It is real and even on the real line, and
\(A(0)=\sum_r p_r(2)^2\ge N^4\). Hence it is nonzero on a
real neighborhood of zero. For any nonzero integer \(n\), the
literal Gaussian multiplier in the filling functional gives
\[
                           g(t)=e^{\pi i nNt^2}A(t).
 \tag{18}
\]
This is even but nonreal at arbitrarily small nonzero real \(t\).
It cannot be positive definite, even locally: positivity of the
two-point Gram matrices requires \(g(-t)=\overline{g(t)}\).
No common scalar phase repairs this, because positivity at zero
would fix that phase to be positive real.

This concerns the specified Gaussian-weighted source. It does not
replace the complete filling functional by a convolution or discard
its original normal terms, charges and endpoint data.

## 5. The positive wire corridor has the same obstruction

The complete samples (7) and the pure wire corridor in the filling
proof are different finite functions. For (3), restricting the
actual wire to \(\mathcal W\subseteq\{H,\ldots,M\}\) gives the
positive pure corridor
\[
 C_N^{\mathcal W}(a/N,b/N)
          =\sum_{r\in\mathcal W}A_{N,r}(a)A_{N,r}(b).
 \tag{19}
\]
Suppose \(\mathcal W\) contains at least two distinct indices. Its
Fourier polynomial has the Gram representation (10) restricted to
these low features, each of degree \(H\). They are not proportional,
because their first two Laurent coefficient ratios are
\[
 \frac{A_{N,r}(1)}{A_{N,r}(0)}
       =\frac{\sin(r\theta)}{\sin((r+1)\theta)},
 \tag{20}
\]
which strictly increase with \(r\). Their consecutive difference
is
\[
 \frac{\sin^2\theta}
      {\sin((r+1)\theta)\sin((r+2)\theta)}>0 .
 \tag{21}
\]
Here only \(r<M\) is needed for consecutive comparisons.

To finish, if a sum of real squares \(\sum_j p_j(u)^2\), of
degree \(2H\), had only real zeros, nonnegativity would write it as
\(cQ(u)^2\), with \(c>0\) and \(\deg Q=H\). At any real zero,
the sum's order is twice the smallest order of its summands:
their first nonzero real leading coefficients have positive sum of
squares. Thus \(Q\) would divide every \(p_j\), forcing all the
degree-\(H\) features to be proportional. This contradicts (20).
The corridor diagonal therefore has a nonreal zero too. The proofs
of nonstability and all four disk/exterior zeros now apply unchanged.

A fixed strict wire window about the complete point contains two
indices at all sufficiently large levels. Choosing the color cutoff
small enough ensures it lies in the range of (19). Thus this version
applies to the positive pure corridor of the filling proof. No
full-minus-core estimate is used to transfer a statement about zeros.

## 6. Scope and complete proof sources

These exact source polynomials do not belong to a universal
real-stable or disk/exterior Lee–Yang class that could extend the
long-filling theorem directly. The literal Gaussian multiplier does
not give a positive-definite substitute.

The argument does not place the zeros relative to an arbitrary
short filling's geometric saddle. A smaller geometric zero-free
domain, a different exact relative-period representation, or a
source-sensitive lower estimate remains possible. The existing
small geometric zero-free neighborhood and the frozen long-filling
theorem are unchanged. No volume identity is proved or disproved.

All three complete proof texts were read at the matching pins below.
The first fixes the full physical turn and pairing, the second the
actual core and signed alias, and the third the strict construction
and component test. The polynomial arguments are proved above.

| Source | SHA-256 |
|---|---|
| [Original Newton turn and Gram](actual_newton_turn_positive_gram.md) | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |
| [Exact pure-circle colors](actual_pure_conway_auxiliary_color_leaf.md) | 2ef360ce60bcaa83969b4900a103573a76290714a59393e17ca25b52f07193c7 |
| [Strict construction definitions](research_strict_conway_family_definitions.md) | 55662159ccd65ae3183bc55b4f17b414d15a18b6970e3d54a725ba16247eeb1a |

The earlier even CROSS stability obstruction concerns a different
face polynomial and is not used here. Fourier positivity, these
zero-free classes and the algebra of Gram kernels are standard;
no general novelty is claimed for them.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or earlier-final edit was performed.
