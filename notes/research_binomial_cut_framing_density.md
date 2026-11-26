# A binomial cut and its polynomially bounded framing density

Private written proof, 18 November 2026.

A single cut occupation near the middle of the physical module
has an exact normal-residue description, but its coefficients at
the two framing endpoints can grow exponentially with the level.
A binomial average of cut occupations avoids that cost. It gives
the same original unmarked knot invariant, and its entire density
on the compact real framing interval has polynomial norm. The
density is a Legendre polynomial evaluation kernel.

The construction below keeps the original marked-current defect.
It does not select a geometric contribution to the invariant.
The complete proof sources are **C**, the actual normal-residue
and cut-moment map; **D**, its whole-clock extension; and **I**,
the exact change of physical cut. Their pins are listed below.
The orthogonal-polynomial calculations are proved here.

## 1. The cut and its exact relation to the original scalar

Fix \(N\ge2\), put \(d=N-1\), and use the factorial basis
\(e_0,\ldots,e_d\) of I. Let \(T_a=e_ae_a^*\) be the diagonal
coordinate projection. Define
\[
 \pi_{N,a}=2^{-d}\binom da,\qquad
 P_N^{\rm cut}=\sum_{a=0}^{d}\pi_{N,a}T_a .
 \tag{1}
\]
The weights are nonnegative and sum to one. Positivity here is
in the stated finite basis metric; no unitary structure on every
quantum-group representation is assumed.

For the actual unmarked one-cut endomorphism, I proves
\(C_N(M)=F_N(M)I\), with the original framing and reduced scalar
normalization. Therefore, exactly at every level,
\[
 \operatorname{Tr}(P_N^{\rm cut}C_N(M))
 =F_N(M)=\operatorname{Tr}(T_0C_N(M)).
 \tag{2}
\]
At \(M=1\) this is the original Kashaev scalar. In particular
no factor such as \(2^{-d}\) is being added to the invariant
after its evaluation; it is part of a trace-one cut probe in (1).

For an arbitrary marked endomorphism the comparison has a defect.
Use I's actual raising coefficients and currents,
\[
 \epsilon_r(M)=M Q^{-r-1}-M^{-1},\quad Q=e^{2\pi i/N},
 \qquad
 B_{N,a}=-\sum_{r<a}\epsilon_r(M)^{-1}E_{r+1,r}.
\]
Set \(B_N^{\rm cut}=\sum_a\pi_{N,a}B_{N,a}\). Then
\[
 [\mathcal E,B_N^{\rm cut}]=P_N^{\rm cut}-T_0,\qquad
 \operatorname{Tr}((P_N^{\rm cut}-T_0)C)
 =\operatorname{Tr}(B_N^{\rm cut}[C,\mathcal E]).
 \tag{3}
\]
Its subdiagonal coefficients are
\(-\Pr(A>r)/\epsilon_r(M)\), where \(A\) has probabilities
\(\pi_{N,a}\). Their numerators have absolute value at most one.
The complete bounds of I consequently give
\[
 \|B_N^{\rm cut}\|\le N/3
 \quad\left(|M-1|\le\frac1{4N}\right),\qquad
 \|\partial_M^j B_N^{\rm cut}\|\le C_jN^{j+1}
 \quad\left(|M-1|\le\frac1{8N}\right)
 \tag{4}
\]
for each fixed \(j\). The same physical tail pivots and marked
word are retained on the right side of (3).

## 2. What a framing density must reproduce

For any finite matrix \(C\), write its diagonal coherent polynomial
as
\[
 \overline f_C(T)=\sum_{a=0}^{d}C_{aa}B_{a,d}(T),\qquad
 B_{a,d}(T)=\binom da T^a(1-T)^{d-a}.
 \tag{5}
\]
This polynomial has degree at most \(d\). It is the angular
average of the full actual coherent symbol in C and D, including
when \(C\) has off-diagonal entries. The exact Toeplitz row is
\[
 [\mathcal T_N(P)]_a
 =N\int_0^1P(-T)B_{a,d}(T)\,dT .
 \tag{6}
\]
The corresponding normal-residue pairing is
\[
 \frac1N\operatorname{Tr}(\mathcal T_N(P)C)
 =\int_0^1P(-T)\overline f_C(T)\,dT .
 \tag{7}
\]
This is a normalized ordinary trace on arbitrary matrices.
As in C and D, its equality with the prescribed average cut
uses diagonality of the actual position-conserving cut arrays.
It is not an equality with that average on arbitrary off-diagonal
Ward matrices. Equation (3) retains the physical comparison.

The density needed for (1) must therefore evaluate all degree
\(\le d\) polynomials at \(T=1/2\):
\[
 \int_0^1p_N(T)q(T)\,dT=q(1/2).
 \tag{8}
\]
Indeed (8) applied to \(B_{a,d}\) gives
\(\mathcal T_N(P_N^{\rm nor})=N P_N^{\rm cut}\), where
\(P_N^{\rm nor}(b)=p_N(-b)\). The factor \(N\) is required
by the original normalization (7).

## 3. An elementary construction of the evaluation kernel

Let \(\mathsf L_k\) denote the ordinary Legendre polynomial,
to distinguish it from the physical circle operators. Define it by
\[
 \mathsf L_k(x)=\frac1{2^kk!}
       \frac{d^k}{dx^k}(x^2-1)^k .
 \tag{9}
\]
Integration by parts \(k\) times shows that it is orthogonal
to every polynomial of degree below \(k\) on \([-1,1]\).
All boundary terms vanish because \((x^2-1)^k\) has a zero
of order \(k\) at both endpoints. Its leading coefficient is
\(2^{-k}\binom{2k}{k}\), and the same integration by parts,
using
\[
 \int_{-1}^1(1-x^2)^k\,dx
       =\frac{2^{2k+1}(k!)^2}{(2k+1)!},
\]
gives
\(\int_{-1}^1\mathsf L_k^2\,dx=2/(2k+1)\).
The displayed integral follows by the substitution
\(x=2u-1\) and the elementary factorial beta integral.
Thus \(\sqrt{2k+1}\mathsf L_k(2T-1)\) is an orthonormal
polynomial basis for Lebesgue measure on \([0,1]\).

Set
\[
 p_N(T)=\sum_{k=0}^{d}(2k+1)\mathsf L_k(0)
                                      \mathsf L_k(2T-1).
 \tag{10}
\]
Expanding \(q\) in this orthonormal basis proves (8), without
an approximation or an asymptotic passage. Consequently
\[
 \boxed{\displaystyle
 \operatorname{Tr}(P_N^{\rm cut}C)
 =\int_0^1p_N(T)\overline f_C(T)\,dT
 =\overline f_C(1/2).}
 \tag{11}
\]
The polynomial density can have either sign. The positive object
in (1) is the physical cut matrix, not its contravariant density.

There is also an exact compact contour presentation. The full
coherent symbol of C and D is
\[
 f_C(v,T)=\sum_{i,j=0}^{d}C_{ij}\binom dj
                         v^{i-j}T^j(1-T)^{d-j}.
\]
Taking its angular constant coefficient gives
\[
 \operatorname{Tr}(P_N^{\rm cut}C)
 =\frac1{2\pi i}\oint_{|v|=1}f_C(v,1/2)\,\frac{dv}{v}.
 \tag{11a}
\]
Thus the compact polynomial density can be integrated out
exactly to an interior latitude circle, for every finite
matrix \(C\). This circle is a co-source presentation;
it has not been identified with the remaining geometric
centralizer quotient.

Here are the elementary bounds used next. Formula (9) gives
\[
 \mathsf L_{2m+1}(0)=0,\quad
 \mathsf L_{2m}(0)=(-1)^m c_m,\quad
 c_m=4^{-m}\binom{2m}{m},\quad
 \mathsf L_k(1)=1,\quad \mathsf L_k(-1)=(-1)^k.
 \tag{12}
\]
It also gives \(|\mathsf L_k(x)|\le1\) for real \(|x|\le1\).
For completeness, its generating series, obtained by expanding
(9), is \((1-2xz+z^2)^{-1/2}\). The same series is obtained by
summing the geometric series under
\[
 \frac1\pi\int_0^\pi
    \bigl(x+i\sqrt{1-x^2}\cos\varphi\bigr)^k\,d\varphi.
\]
Indeed the normalized integral \(\pi^{-1}\int_0^\pi\) of
\((1-zx-iz\sqrt{1-x^2}\cos\varphi)^{-1}\) is
\(((1-zx)^2+z^2(1-x^2))^{-1/2}\); the substitution
\(\tan(\varphi/2)\) verifies it near \(z=0\), with branch one
there. Each base in the integrand has modulus at most one.
Comparison of coefficients proves the bound.

## 4. Exact endpoint and norm formulas

Put \(m_*=\lfloor d/2\rfloor\) and
\(A_N=(2m_*+1)c_{m_*}>0\). Then
\[
 \boxed{\displaystyle
 p_N(0)=p_N(1)=(-1)^{m_*}A_N,\qquad
 \|p_N\|_{L^2(0,1)}=A_N.}
 \tag{13}
\]
Here is a direct verification. The endpoint sum is
\(\sum_{m=0}^{m_*}(4m+1)(-1)^m c_m\).
The ratio \(c_m/c_{m-1}=(2m-1)/(2m)\) shows by subtraction
that its partial sum is
\((-1)^{m_*}(2m_*+1)c_{m_*}\).
Orthogonality gives
\[
 \|p_N\|_2^2=\sum_{m=0}^{m_*}(4m+1)c_m^2
                         =(2m_*+1)^2c_{m_*}^2.
\]
The last equality telescopes by the same ratio.
Induction on that ratio proves \(c_m^2\le1/(m+1)\).
Hence \(A_N\le2\sqrt N\), including \(N=2\), and
\[
 \|p_N\|_{L^1(0,1)},\ \|p_N\|_{L^2(0,1)}\le2\sqrt N,
 \qquad
 \|p_N\|_{L^\infty(0,1)}\le N A_N\le2N^{3/2}.
 \tag{14}
\]
The supremum bound follows from Cauchy--Schwarz in (10):
the evaluation vector at \(T\) has squared norm at most
\(\sum_{k=0}^{d}(2k+1)=N^2\), while that at \(1/2\)
has norm \(A_N\).

All fixed real derivatives also have polynomial bounds:
\[
 \|p_N^{(r)}\|_\infty
                  \le(2N^2)^r N A_N .
 \tag{15}
\]
To see this without importing a derivative inequality, expand
\(\mathsf L_k'\) in the Legendre basis. Integration by parts
and (12) give coefficient \(2\ell+1\) at every
\(\ell<k\) of parity opposite to \(k\), and zero otherwise.
Their sum is \(k(k+1)/2\le N^2\). Repeating this expansion
at each derivative and using the factor two from \(2T-1\)
proves (15). Cauchy--Schwarz bounds the original coefficient
sum in (10) by \(N A_N\).
In particular, on the complex distance-\(\delta\)
neighborhood of \([0,1]\), Taylor's finite formula gives
\[
 |p_N(T)|\le N A_N\exp(2N^2\delta).
 \tag{16}
\]
This supplies a polynomial bound on collars of width
\(O(N^{-2})\), not on a fixed complex neighborhood.

## 5. The actual normal residue and its retained current

In the normal framing coordinates of C and D,
\(b_N=-a/\eta\), \(T=va\), and
\[
 \nu_{\rm cut}=-\frac{d\eta}{\eta}\wedge
                       \frac{\Omega}{1-\eta v}.
\]
The exact finite residue is
\[
 \operatorname{Res}_E
       [P_N^{\rm nor}(b_N)\nu_{\rm cut}]
                            =-p_N(T)\Omega .
 \tag{17}
\]
With the original compact-cycle normalization, pairing (17)
against the actual coherent source gives (11). The compatible
south representative remains \(P_N^{\rm nor}(b_S-1)\).
No change of the affine clutch or deletion of \(1-\eta v\)
before the residue is made.

The degree is \(2m_*\), so the normal pole order is \(2m_*+1\):
it is \(N\) at odd levels and \(N-1\) at even levels.
The polynomial compact residue bounds do not turn this into
a bounded normal jet or identify the off-divisor source with
its residue.

The two density endpoints in (13) agree, but the full current
does not consequently vanish. For arbitrary diagonal \(C\),
the actual integration-by-parts map is
\[
 \boxed{\displaystyle
 \frac1N\operatorname{Tr}
       (\mathcal T_N((P_N^{\rm nor})')C)
 =(-1)^{m_*}A_N(C_{00}-C_{dd})
       +\overline f_C'(1/2).}
 \tag{18}
\]
Indeed the endpoint formula in C gives the first term and
the remaining integral is
\(\int_0^1p_N(T)\overline f_C'(T)\,dT\).
Here \(\overline f_C'\) has degree at most \(d-1\), so (8)
evaluates that integral exactly. Explicitly
\[
 \overline f_C'(1/2)
 =d\sum_{a=0}^{d-1}2^{-(d-1)}\binom{d-1}{a}
                                  (C_{a+1,a+1}-C_{aa}).
\]
This includes \(N=2\). For \(C=I\) both terms vanish;
for a marked source neither is to be omitted.
The product-current correction of C is still present before
pairing.

## 6. Scope of the new presentation

The cut probabilities are concentrated near the middle
occupation. Precisely
\[
 \Pr(|A-d/2|\ge\varepsilon d)
                  \le2e^{-2\varepsilon^2d}.
 \tag{19}
\]
An elementary proof uses
\(\mathbb E e^{t(A-d/2)}=\cosh(t/2)^d\le e^{dt^2/8}\)
and exponential Markov inequality with \(t=4\varepsilon\).
The hyperbolic-cosine bound follows by integrating
\(\tanh x\le x\). The estimate describes the probe weights;
discarding their tails in a marked contraction also needs a
bound on that contraction's matrix entries.

Equation (11) gives a fixed interior latitude evaluation of
the angularly averaged coherent source. In I's existing
classical cut-position chart, the central occupation has
the noncentral complete parameter \(s=-2\). This does not
prove that the full new quantum source has just the old
geometric critical point or the same stationary equations.
An exponentially varying matrix kernel can shift a saddle
in a binomial sum. Its entropy and all remaining variables
must be retained in a new source analysis.

What is settled is a source-preserving choice of cut with a
polynomially bounded compact framing density and exact current.
The remaining centralizer coordinate, off-divisor normal
transport, transverse source map, and geometric cycle
coefficient are not supplied by this calculation. No new
volume-conjecture filling case is claimed.

## Coverage and complete proof-source pins

The polynomial evaluation kernel and its orthogonality belong
to classical orthogonal-polynomial theory; see
[DLMF, Section 18.2(v)](https://dlmf.nist.gov/18.2#v)
and [the classical normalizations](https://dlmf.nist.gov/18.3).
No novelty is claimed for them. The proof above derives the
identities needed for the particular physical cut. The
literature was consulted for coverage, not as a substitute
for those derivations.

* C: notes/centralizer_normal_residue_and_actual_cut_moments.md,
  SHA256 b040461ba07902277ae2964515060e4927322f30c0be81772bed7f2d3da72a1a.
* D: notes/dual_clock_normal_cut_source.md,
  SHA256 73191e0560d48789aaacebb44c1c768f66f4c3c3f3ecf8af3faf1380d69eafa3.
* I: notes/research_fixed_interior_cut_source.md,
  SHA256 93b2887527e0b5c9cb93f4da77702c996f0524e0a93f0c0032909345efdbd1b2.

All three complete directs were read nontruncated in the author
sequence, their used implications checked, and their matching
pins renewed. Only written mathematics and text/hash operations
were used; frozen/public files are unchanged.
