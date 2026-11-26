# One-sided representatives of the complete angular Hermite data

Research calculation, 3 November 2026. The original trace can be
written as one coefficient of a polynomial containing only
nonnegative angular Fourier frequencies. This is an exact change
of representative. It does not by itself give a lower bound for
that coefficient or discard a contour contribution.

The Fourier--Hermite coordinates in
[the filling Gram calculation](actual_filling_fourier_hermite_gram.md)
already retain all physical values and first normals. Here we use
the angular variable to describe a different representative of the
same data. This is separate from the internal head projections in
[the Hardy kernel construction](actual_hardy_cauchy_network.md).

## 1. The angular quotient and its one-sided representative

Fix an integer level \(N\ge3\), and put
\[
 \eta=(-1)^{N-1},\qquad z=e^{-it},\qquad
 t_j=\frac{\pi(N-1-2j)}N\quad(0\le j<N).
 \tag{1}
\]
The points \(z_j=e^{-it_j}\) are the distinct roots of
\(z^N=\eta\). In the original spectral variable
\(w=-2\cos t=-z-z^{-1}\), the defining relation satisfies
\[
 2T_N(w/2)+2=(-1)^Nz^{-N}(z^N-\eta)^2.
 \tag{2}
\]
Indeed \(2T_N(-(z+z^{-1})/2)=(-1)^N(z^N+z^{-N})\),
and \((-1)^N\eta=-1\). Thus replacing a Laurent polynomial
modulo \((z^N-\eta)^2\) preserves its full physical Hermite
data. At an ordinary double spectral node the change of variable
has nonzero derivative. At the odd simple endpoint \(w=-2\),
the ramification explains the angular double zero in (2);
there is no missing spectral normal at that endpoint.

**Proposition 1.** Every Laurent polynomial has a unique
representative of degree less than \(2N\) modulo
\((z^N-\eta)^2\). Write an integer frequency as
\(m=a+\ell N\), where \(0\le a<N\) and \(\ell\in\mathbb Z\).
Its representative is
\[
 \mathcal H_N(z^m)
 =\eta^\ell\bigl((1-\ell)z^a+\ell\eta z^{a+N}\bigr).
 \tag{3}
\]
In particular, for \(1\le k<N\),
\[
 \mathcal H_N(z^{-k})=2\eta z^{N-k}-z^{2N-k}.
 \tag{4}
\]

**Proof.** The polynomial \((z^N-\eta)^2\) has nonzero
constant coefficient, so \(z\) is invertible in its quotient.
The usual polynomial remainder is therefore defined for every
Laurent monomial and is unique in degrees below \(2N\).
With \(x=z^N\), Taylor expansion modulo \((x-\eta)^2\)
gives
\[
 x^\ell=\eta^\ell+\ell\eta^{\ell-1}(x-\eta)
        =\eta^\ell(1-\ell)+\ell\eta^{\ell-1}x.
\]
This holds for negative integers as well, since \(x\) is a unit.
Multiplying by \(z^a\) proves (3), and \(\ell=-1\) proves
(4). \(\square\)

The map is linear and preserves products after reduction:
\(\mathcal H_N(fg)=\mathcal H_N(\mathcal H_N(f)
\mathcal H_N(g))\). Thus it can be applied to each edge
factor before forming an original vertex product, provided the
final product is interpreted in the same quotient. It is not
an identity of ordinary functions away from the physical grid.

## 2. The original trace becomes a coefficient

Write
\[
 C_{N,n}=\exp\frac{\pi i n(N-1)^2}{4N},\qquad
 g(t)=\sin t\, f(t)\exp\frac{inNt^2}{4\pi}.
 \tag{5}
\]
The complete derivative-sampling identity is
\[
 \mathcal D_{n,N}[f]=\eta C_{N,n}\sum_{j=0}^{N-1}g'(t_j).
 \tag{6}
\]
It includes the full normals and both level parities, as proved in
[the exact trace calculation](research_exact_complete_trace_contour.md).

Let \(G_N(z)\) be the degree-less-than-\(2N\) Hermite
interpolating polynomial characterized by
\[
 G_N(z_j)=g(t_j),\qquad
             -iz_jG_N'(z_j)=g'(t_j).
 \tag{7}
\]
This definition is valid even when the chirp in (5) is not
periodic in \(t\): it prescribes finite jets at distinct points,
not a global logarithm on the punctured plane.

**Proposition 2.** With the original normalization,
\[
 \boxed{\mathcal D_{n,N}[f]
             =-iN^2C_{N,n}[z^N]G_N(z).}
 \tag{8}
\]

**Proof.** If \(G_N(z)=\sum_{a=0}^{2N-1}c_a z^a\), then
\(\sum_jz_j^a=0\) unless \(N\mid a\). Consequently
\[
 \sum_j(-iz_jG_N'(z_j))=-iN^2\eta c_N.
\]
Insert this equality in (6) and use \(\eta^2=1\).
\(\square\)

Equation (8) is also a Cauchy coefficient integral on any
circle centered at zero. It contains no angular endpoint
terms, because the finite interpolation has already incorporated
all the original jets into \(G_N\). To turn it into a volume
estimate, one must estimate the coefficient \([z^N]G_N\).
The formula does not supply that estimate.

## 3. A filter and the exact contour term it moves

Put \(y=\eta z^N\) and consider
\[
 L_N(z)=2\eta z^N-z^{2N}=2y-y^2=1-(1-y)^2.
 \tag{9}
\]
At every physical point, \(L_N=1\) and \(L_N'=0\).
Multiplication by \(L_N\) consequently preserves all trace
jets. On a lower angular line, where \(|z|<1\), it suppresses
the original function by a power of \(z^N\). The corresponding
change in the residue kernel is exactly
\[
 L_N(z)\frac{z^N}{(1-\eta z^N)^2}
 =\frac{z^N}{(1-\eta z^N)^2}-z^N.
 \tag{10}
\]
There is no asymptotic remainder in this identity.

For a rectangular angular contour enclosing the desired grid
points, the unpaired derivative-residue formula is
\[
 \mathcal D_{n,N}[f]
 =-\frac{N^2C_{N,n}}{2\pi i}
       \oint g(t)\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}\,dt.
 \tag{11}
\]
Indeed the kernel multiplied by \(-N^2\eta\) has leading
term \((t-t_j)^{-2}\) and no simple-pole term at each grid
point. Its residue against \(g\) is \(g'(t_j)\).

After multiplication by \(L_N\), (10) changes (11) by the
integral of the entire function \(g(t)e^{-iNt}\), whose closed
contour integral is zero. On separate contour sides this term
need not vanish. In particular, removing the first Fourier mode
from the lower side transfers that same mode to the upper and
vertical sides. The new representative is not even, so the
previous evenness folding cannot simply be reused.

This identifies the additional estimate required for a useful
one-sided replacement: the transferred entire term must either
cancel in the exact assembled contour or have a proved strict
rate bound there.

## 4. Positivity is not created by this projection

Even positive Laurent coefficients are not preserved. For
\(N\ge3\),
\[
 2+z+z^{-1}\quad\longmapsto\quad
             2+z+2\eta z^{N-1}-z^{2N-1}.
 \tag{12}
\]
The input is nonnegative on the unit circle, but the one-sided
representative has a negative top coefficient at every level.
Thus coefficient positivity cannot be inferred merely from the
choice of nonnegative frequencies.

Nor does an unrestricted boundary turn preserve the existing
positive-volume source class. With the original matrices,
\(H_{a,N}=JM^a\mathbf e_0\) satisfies
\(JH_{a,N}=M^a\mathbf e_0\). For odd \(N\), the complete
point is physical, and the latter source has value
\(C_{N,a}\) there, of modulus one. This suffices to exclude
preservation of the terminal source's positive exponential rate
under an arbitrary additional turn. The odd-level qualification
is essential; an off-grid even-level evaluation is not being
identified with a physical crossing value.

The exact projection therefore gives a different representation
of the remaining cancellation problem. A successful lower-bound
argument must still use a property of the actual coefficient,
the transferred contour term, or an inner product adapted to
the original source.

## 5. A coefficient of the actual polynomial source

The same identity can be written entirely in the original quotient
algebra, without the chirp or the interpolation problem in (7).
Put \(D=N-1\) and
\[
 \mathcal A_N=\mathbb C[w]/(P_N(w)),\qquad
 P_N(w)=2T_N(w/2)+2.
 \tag{13}
\]
The original complete trace is
\(\phi_N(f)=\eta N^2[w^D]\operatorname{rem}_{P_N}f\).
The normalization is the one in
[the finite-source formula](../papers/circle-tree-volume/finite-bounds.tex).

**Proposition 3.** For every \(f\in\mathcal A_N\),
\[
 \boxed{\displaystyle
 \phi_N(f)=\frac{N^2}{2}[z^N]\mathcal H_N
       \bigl[(z-z^{-1})f(-z-z^{-1})\bigr].}
 \tag{14}
\]
Any polynomial representative of \(f\) gives the same right-hand
side.

**Proof.** Independence of the representative follows from (2):
the pullback of a multiple of \(P_N\) is zero modulo
\((z^N-\eta)^2\), also after multiplication by \(z-z^{-1}\).
It therefore suffices to consider \(f(w)=w^k\), \(0\le k\le D\).
For \(k<D\), every frequency of
\((z-z^{-1})(-z-z^{-1})^k\) lies strictly between \(-N\) and
\(N\). Formula (3) shows that none of those frequencies contributes
to \(z^N\), including frequency zero.

For \(k=D\), the two extreme terms are
\(\eta z^N-\eta z^{-N}\); all other frequencies lie strictly
between them. Formula (3) gives
\(\mathcal H_N(z^{-N})=2\eta-z^N\), so the coefficient of
\(z^N\) is \(2\eta\). The right-hand side of (14) is thus
\(\eta N^2\) on \(w^D\) and zero on all lower monomials,
exactly as required. \(\square\)

To state the tensor version, let \(\Gamma=(V,E)\) be a fixed
finite graph whose original source is the product of the complete
edge kernels. Let \(I\subseteq V\) be its selected vertices,
with \(m=|I|\), and write
\[
 \mathcal K_N(w_v,w_w)=
       \sum_{j=0}^{D}e_j(w_v)e_j(w_w),\qquad
 w_v=-z_v-z_v^{-1}\quad(v\in I).
 \tag{15}
\]
Unselected boundary values are retained as parameters; a complete
boundary has \(w_v=-2\). Let \(R_N\in\mathcal A_N\) be the
original crossing element. It is a unit, so \(R_N^{n_v}\) is
defined in the quotient for every signed integer \(n_v\).
Keep its original carrier and scalar conventions. Define the
Laurent polynomial, with these quotient representatives inserted,
by
\[
 \mathcal F_N(\mathbf z)=
 \prod_{v\in I}(z_v-z_v^{-1})R_N^{n_v}(w_v)
                  \prod_{\{v,w\}\in E}\mathcal K_N(w_v,w_w).
 \tag{16}
\]

**Corollary 4.** The original coupled contraction satisfies
\[
 \boxed{\displaystyle
 Z_{\Gamma,I,N}
 =\left(\frac{N^2}{2}\right)^m
    \left[\prod_{v\in I}z_v^N\right]
        \mathcal H_N^{\otimes I}\mathcal F_N(\mathbf z).}
 \tag{17}
\]
The polynomial after projection has degree less than \(2N\)
in each selected variable. All factors on a shared vertex are
multiplied before its trace is taken.

**Proof.** Apply (14) in each selected variable. The trace maps,
the reductions in distinct variables, and the coefficient extractions
commute because they are finite linear operations in separate tensor
factors. Equation (2) makes (17) independent of every chosen
representative of a signed crossing power. Each original edge
appears once in (16); no coupling or first normal is discarded.
\(\square\)

Equation (17) is an identity of the actual finite polynomial source.
In particular, it does not require a continuous crossing power or
an off-grid logarithm of the crossing matrix. Its possible use in
asymptotics is to group the original quotient relations before
estimating a single multivariate coefficient. A nonzero geometric
leading coefficient remains an additional statement to prove.

**Corollary 5.** Let
\(Q_N=\mathcal H_N^{\otimes I}\mathcal F_N\) be the actual
projected polynomial in (17). Then
\[
 \boxed{\displaystyle
 Z_{\Gamma,I,N}=
       \left(-\frac{\eta N^2}{2}\right)^m Q_N(0,\ldots,0).}
 \tag{18}
\]

**Proof.** Before projection, (16) is anti-reciprocal in each
selected variable: replacing \(z_v\) by \(z_v^{-1}\) changes
its sign. The physical grid is closed under inversion, so the
sum of its values over that grid is zero, with every other
variable held fixed. Projection preserves those values. For a
polynomial \(Q(z)=\sum_{a=0}^{2N-1}c_a z^a\), their sum is
\(N(c_0+\eta c_N)\). Thus \(c_N=-\eta c_0\) in each
selected variable. These coefficient maps commute in distinct
variables. Applying them successively to (17) gives (18).
\(\square\)

This evaluation is exactly the central coefficient in (17),
written in different coordinates. Its value still depends on
the level through the original source and its Hermite projection.
In particular, (18) supplies no analytic lower bound and does
not establish its exponential growth rate. At odd levels,
\(\eta=1\), so a real nonzero one-variable source already
has opposite constant and central coefficients; this also
precludes a naive coefficient-positivity argument in this
representation.

## 6. An actual source with a large Hardy norm and a small evaluation

The new representative does not turn the original closing evaluation
into a norm lower bound. This can be seen in a fixed original tangle,
without an engineered linear combination.

Fix an even integer \(a\ge4\). Let
\[
 f_N(w)=T(R_N^a)(w),\qquad
 Q_N(z)=\mathcal H_N\!\left[
       (z-z^{-1})f_N(-z-z^{-1})\right].
 \tag{19}
\]
Thus \(f_N(-2\cos u)=H_{a,N}(u)\) is the original terminal
source, including all its normal data. Its
[proved terminal expansion](research_uniform_terminal_family_and_star_fillings.md)
gives
\[
 |f_N(-2)|=\exp\{NM_a+O_a(\log N)\},\qquad M_a>0.
 \tag{20}
\]
For \(4\le a\le31\), positivity of the rate is also explicit in
[the finite-power terminal proof](research_terminal_powers_four_through_thirty_one.md);
for \(a\ge32\), it follows from
[the large-power estimate](research_terminal_large_fixed_powers.md).
The power \(a\) is fixed before \(N\) tends to infinity.

The exact closing value, however, has modulus one. To check its
normalization, write \(g=\sum_{j=0}^{D}g_j e_j\). The
[Newton turn and closure identities](../papers/newton-calculus/finite.tex)
give
\[
 \phi_N(Tg)=g_0=g(c_0),\qquad c_0=2\cos(\pi/N).
 \tag{21}
\]
Here \(e_j(c_0)=0\) for \(j>0\), \(\phi_N(e_D)=1\), and
\(T e_j=e_{D-j}\). In particular (21) is evaluation at \(c_0\),
not at the complete point \(-2\). The original crossing formula
has \(R_N(c_0)=\kappa_N\), where
\(\kappa_N=\exp(\pi iD^2/(2N))\). Hence
\[
 \phi_N(f_N)=\kappa_N^a,\qquad
                         |Q_N(0)|=\frac2{N^2}
 \tag{22}
\]
by (18).

Define the ordinary Hardy norm of a polynomial by
\[
 \left\|\sum_{j=0}^{2N-1}c_jz^j\right\|_{H^2}^2
   =\sum_{j=0}^{2N-1}|c_j|^2
   =\frac1{2\pi}\int_{-\pi}^{\pi}|Q_N(e^{it})|^2\,dt .
 \tag{23}
\]
At every odd level, \(\eta=1\) and \(z=1\) is a physical
angular point. Hermite preservation therefore implies
\[
 Q_N'(1)
   =\left.\frac{d}{dz}
       \{(z-z^{-1})f_N(-z-z^{-1})\}\right|_{z=1}
   =2f_N(-2).
 \tag{24}
\]
This uses the angular derivative at the ramified odd endpoint;
it does not assert an extra spectral normal there. At even levels
\(z=1\) is off the grid, so (24) is not being imposed.

Cauchy--Schwarz and the exact degree bound give
\[
 \begin{split}
 |Q_N'(1)|
   &\le \|Q_N\|_{H^2}
                 \left(\sum_{j=0}^{2N-1}j^2\right)^{1/2},\\
 \sum_{j=0}^{2N-1}j^2
   &=\frac{(2N-1)(2N)(4N-1)}6<\frac83N^3.
 \end{split}
 \tag{25}
\]
Consequently, along odd levels,
\[
 \|Q_N\|_{H^2}\ge
       \sqrt{\frac32}\,N^{-3/2}|f_N(-2)|,\qquad
 \frac{|Q_N(0)|}{\|Q_N\|_{H^2}}
           \le \exp\{-NM_a+O_a(\log N)\}.
 \tag{26}
\]
The odd subsequence already excludes a general subexponential
lower comparison between evaluation and this norm.

The same conclusion holds for every positive coefficient metric
whose condition number is subexponential. Precisely, let \(v_N\)
be the coefficient vector of \(Q_N\), and let
\(\mathbf e_0=(1,0,\ldots,0)^{\mathsf T}\).
For a positive Hermitian matrix \(G_N\), the norm of evaluation
at zero in its dual metric is
\((\mathbf e_0^*G_N^{-1}\mathbf e_0)^{1/2}\). Thus
\[
 \frac{|\mathbf e_0^*v_N|}
      {(v_N^*G_Nv_N)^{1/2}
       (\mathbf e_0^*G_N^{-1}\mathbf e_0)^{1/2}}
 \le
 \sqrt{\operatorname{cond}(G_N)}
                \frac{|Q_N(0)|}{\|Q_N\|_{H^2}}.
 \tag{27}
\]
Indeed the squared denominator on the left is at least
\(\|v_N\|_2^2/\operatorname{cond}(G_N)\). If
\(\log\operatorname{cond}(G_N)=o(N)\), (26)--(27) give an
exponentially small normalized evaluation. Rescaling the metric
does not alter this conclusion.

The cylindrical closure of \(T(R_N^a)\) is an unknot with
removable curls; its unit value in (22) is the expected geometric
loss under that closure. This example therefore does not
contradict a lower bound for a specified admissible hyperbolic
composition that includes its change of volume. It shows that
the one-sided representative, positivity of a Hardy or Toeplitz
norm, and subexponential conditioning do not supply such a lower
bound on their own.
