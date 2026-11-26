# An actual complex-clock packet for the opened generator

Private written proof, 19 November 2026.

The original opened crossing has a nonzero, explicitly marked packet
period whose three independent occupation coordinates can move into a
complex open set. Total degree is summed, not fixed. The selected
critical total clock can therefore have modulus different from one.
The coefficient comes from a deformation of the literal finite lattice
residue cycle. All cap terms, rectangular connectors, and nonzero
cotangent modes are retained and estimated.

This is a packet-marked local source statement. It does not identify
the packet with a complementary Gauss image, an exterior supplied by
a knot, or a geometric contribution to a closed source. The complete
directs are W and F, pinned below. W gives the actual opened matrix
and coherent annuli; F gives the exact factorial interpolation.

## 1. Literal packets, three occupations, and all marks

Put \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), \(x=-q^{-1}\), and
\(\mathfrak s_j=\prod_{k=1}^j2\sin(\pi k/N)\).
The meridian is fixed at one. On the actual two-head space the opened
generator \(X=\kappa S_2D\) preserves total occupation \(T\). W proves
\[
 X_{(c,T-c),(a,T-a)}
 =\kappa(-1)^c q^{(T+c+2)a-(T+1)c}
       \frac{\mathfrak s_{T-c}}
            {\mathfrak s_{a-c}\mathfrak s_{T-a}},
 \qquad 0\le c\le a\le T\le d.                         \tag{1}
\]
The other entries in these degree blocks vanish. We use the literal
nonzero scalar \(\kappa=\kappa_N\), without changing its normalization.

Choose integer centers \(A,B,C,D\) with
\[
 A+B=C+D=T_*,\qquad
 v_*=(\tau_*,\eta_*,\xi_*)=(T_*,A,C)/N
        \in K\Subset\{0<\xi<\eta<\tau<1\}.              \tag{2}
\]
Choose positive even integers \(L_i\), \(i=1,\ldots,4\), with
\(\delta_i=L_i/N\) in a fixed small compact interval of positive
numbers. The centers in order are \(A,B,C,D\). The widths are small
enough that every conserved tuple in the four supports below obeys
the strict inequalities in (1), with a common positive scaled margin
from every physical wall. In particular its total degree is at most
\(d\) for all large \(N\). Such widths exist uniformly on \(K\).

For a center \(m_i\) and width \(L_i\), define the literal finite packet
\[
 b_i(k)=
 \begin{cases}
 \displaystyle\frac{2^{-L_i}\binom{L_i}{k-m_i+L_i/2}}{\nu_{L_i}},
                   &m_i-L_i/2\le k\le m_i+L_i/2,\\
 0,&\text{otherwise},
 \end{cases}
 \qquad
 \nu_L^2=4^{-L}\binom{2L}{L}.                           \tag{3}
\]
Each has Euclidean occupation norm one. All indices in (3) are
integers: the even-width convention removes any parity ambiguity.
Their tensor products give a literal input vector and an algebraic
output row. No Hermitian-conjugation rule is imposed when parameters
below are continued holomorphically.

Use the three coordinates
\[
 v=(\tau,\eta,\xi)=(T,a,c)/N,\qquad
 \ell_1v=\eta,\quad \ell_2v=\tau-\eta,\quad
 \ell_3v=\xi,\quad \ell_4v=\tau-\xi.                    \tag{4}
\]
Set \(J(t)=\int_0^t\log(2\sin\pi s)\,ds\), and
\[
 R(v)=J(\tau-\xi)-J(\eta-\xi)-J(\tau-\eta).
                                                               \tag{5}
\]
The exact finite phase in (1), rather than just its principal part, is
\[
 \vartheta_N(v)=
 \pi(\tau\eta+\xi\eta-\tau\xi+\xi)
                   +\frac{\pi}{N}(2\eta-\xi).          \tag{6}
\]
Thus the phase in (1) is \(e^{iN\vartheta_N(v)}\), including
\((-1)^c\) and both finite \(q\) shifts.

For a complex tilt \(z\in\mathbb C^3\), define the actual finite period
\[
 \begin{split}
 \mathcal P_N(z)=
 \sum_{T,a,c}& b_1(a)b_2(T-a)b_3(c)b_4(T-c)
                 X_{(c,T-c),(a,T-a)}\\
 &\times
 \exp\{N[-\nabla R(v_*)-i\nabla\vartheta_N(v_*)+z]
                                      \cdot(v-v_*)\}.
 \end{split}                                                   \tag{7}
\]
The sum is over physical indices; packets outside their exact caps
are zero. In particular it includes the actual total-degree sum.
All linear weights in (7) are genuine input/output diagonal frames:
for example \(N(L_\tau\tau+L_\eta\eta+L_\xi\xi)\) equals
\((L_\tau+L_\eta)a+L_\tau(T-a)+L_\xi c\).
The centered constant in (7) remains part of the period. It has not
been dropped as a common-degree scalar.

The marked phase is fixed by the original factorial convention.
Indeed F gives
\(\widehat F_N(s)=e^{i\pi s(s+1)/(2N)-i\pi s/2}G_N(s)\),
where \(G_N(j)=\mathfrak s_j\).
In the ratio in (1), the difference of the linear factorial
arguments is zero and the quadratic difference is
\(2(a-c)(T-a)\). Combining this with
\(x^{-(a-c)}(-1)^a q^{a(a+1)}\), using
\(\Log x=i\pi-\pi i/N\), gives exactly (6), also off the lattice.
There is no new periodic interpolation factor.

## 2. Phase, nonzero coefficient, and complex total clock

Let \(h(p)=-p\Log p-(1-p)\Log(1-p)\), on its branch near \(1/2\),
and put \(\Delta=v-v_*\) and
\[
 p_i(v)=\frac12+\frac{\ell_i\Delta}{\delta_i},\qquad
 Q_0(\Delta)=\pi(\Delta_\tau\Delta_\eta+
                 \Delta_\eta\Delta_\xi-\Delta_\tau\Delta_\xi).
\]
The relevant holomorphic phase is
\[
 \Phi_z(v)=R(v)-\nabla R(v_*)\cdot\Delta
       +\sum_{i=1}^4\delta_i[h(p_i(v))-\log2]
       +iQ_0(\Delta)+z\cdot\Delta.                     \tag{8}
\]
All sine logarithms are continued from the protected real intervals.
The data \(v_*,\delta_i\) are their exact \(N\)-dependent values.
They are not replaced by limits in either phase or amplitude.

There is a fixed nonempty tilt polydisk, uniform over the chosen
compact data, on which \(\Phi_z\) has a unique critical point
\(v_z\) near \(v_*\). Write
\[
 \Phi_*(z)=\Phi_z(v_z),\qquad H_z=-\Phi_z''(v_z).
\]
Define
\[
 a(v)=
 \sqrt{\frac{\sin\pi(\tau-\xi)}
            {2\sin\pi(\eta-\xi)\sin\pi(\tau-\eta)}}
 \prod_{i=1}^4
       \frac{(\pi\delta_i)^{-1/4}}
            {\sqrt{2p_i(v)(1-p_i(v))}}.               \tag{9}
\]
The square roots are positive on the real protected locus and
continued in the indicated local tube. Then
\[
 \boxed{\quad
 \mathcal P_N(z)=
 \kappa e^{iN\vartheta_N(v_*)}
 e^{N\Phi_*(z)}
 \frac{(2\pi)^{3/2}a(v_z)}{\sqrt{\det H_z}}
                         (1+O(N^{-1})).
 \quad}                                               \tag{10}
\]
The coefficient is holomorphic and nonzero. The determinant branch
is specified below by the actual oriented real Gaussian. All fixed
tilt derivatives of the normalized relative error obey the same
bound on a smaller polydisk.

The map \(z\mapsto v_z\) is locally biholomorphic at zero. In
particular its image contains a complex open neighborhood of
\(v_*\), not just points of real total degree. Its inverse is explicit
on a sufficiently small neighborhood:
\[
 z(v)=\nabla R(v_*)-\nabla R(v)
       -\sum_i\ell_i^t\Log\frac{1-p_i(v)}{p_i(v)}
       -i\nabla Q_0(v-v_*).                           \tag{10a}
\]
All logarithms retain the branches fixed at the real center.
For an insertion of
the actual total Cartan on the input, the same proof gives
\[
 \frac{\mathcal P_N[K_{\rm tot};z]}{\mathcal P_N(z)}
       =x^2e^{-2\pi i(\tau_z)}(1+O(N^{-1})).            \tag{11}
\]
Individual input and output clocks have the corresponding symbols
\(x e^{-2\pi i\ell_i v_z}\). The insertion notation means the same
finite sum multiplied by the literal diagonal clock eigenvalue,
not a noninteger matrix evaluation.
For \(\Im\tau_z\ne0\), the leading total-clock modulus in (11) is
different from one.

This statement concerns a non-Hermitian bilinear period. It is
consistent with the fact that the physical Cartan is unitary up to
\(|x|\) in a positive occupation metric. No positive-state
approximate eigenvector outside its spectrum is asserted.

## 3. The real maximum and the exact interpolant

The real support of (7), in scaled coordinates, is the intersection
of the four packet intervals with the conservation hyperplane (4).
It is convex. On it all three arguments in (5) remain in protected
subintervals of \((0,1)\).
The triangle entropy \(R\) is concave in
\((u,v)=(\eta-\xi,\tau-\eta)\): W's two-variable Hessian, or direct
cotangent addition, has negative diagonal entries and determinant
\(\pi^2\). Its pullback to the three coordinates is negative
semidefinite. Therefore
\[
 R(v)-\nabla R(v_*)\cdot\Delta\le R(v_*).
 \]
Since \(h''(p)=-1/[p(1-p)]\le-4\),
\[
 \Re\Phi_0(v)
 \le R(v_*)-2\sum_i\frac{(\ell_i\Delta)^2}{\delta_i}
 \le R(v_*)-c|\Delta|^2                              \tag{12}
\]
on the whole real support, including its endpoints by continuity.
The four forms in (4) span the three-dimensional dual space; this
proves the last uniform inequality and strict negativity of the
real Hessian. The imaginary quadratic in (8) changes neither fact.
Consequently \(H_0\) has positive-definite real part and is
invertible. The holomorphic implicit-function theorem gives \(v_z\);
its derivative is \(H_0^{-1}\), proving the open-image assertion.

For the exact interpolation in a protected complex neighborhood,
replace \(\mathfrak s_j\) by F's \(G_N(j)\), without changing (6).
Replace each packet's binomial coefficient by
\[
 \frac{\Gamma(L_i+1)}
 {\Gamma(N\ell_i v-m_i+L_i/2+1)
  \Gamma(L_i-N\ell_i v+m_i-L_i/2+1)}.                  \tag{13}
\]
Keep \(2^{-L_i}/\nu_{L_i}\) exactly. Call the resulting summand,
after dividing by \(\kappa e^{iN\vartheta_N(v_*)}\),
\(I_N(v;z)\). It equals the literal summand at every lattice
point in the neighborhood.
It is holomorphic and nonzero there: the sine-factorial arguments
have scaled real parts strictly between zero and one, and the
Gamma arguments in (13) have positive real parts.

F's uniform complex expansion and ordinary Stirling expansion in
these fixed right-half-plane sectors give
\[
 I_N(v;z)=N^{-3/2}a(v)e^{N\Phi_z(v)}(1+O(N^{-1})).
                                                               \tag{14}
\]
This is an expansion on the whole complex neighborhood, with
holomorphic uniform error, not an error known only at lattice
samples. In detail, the sine ratio supplies \(N^{-1/2}\) times
the first factor of (9). Each packet supplies
\[
 N^{-1/4}
 \frac{(\pi\delta_i)^{-1/4}}{\sqrt{2p_i(1-p_i)}}
 e^{N\delta_i[h(p_i)-\log2]}(1+O(N^{-1})),
\]
using \(\nu_{L_i}=(\pi L_i)^{-1/4}(1+O(N^{-1}))\).
The four packet powers and the sine-ratio power give exactly
\(N^{-3/2}\).

Outside a fixed small real cube about \(v_*\), the original finite
sum is exponentially smaller than \(e^{NR(v_*)}\).
For a direct bound at all packet caps, use
\(\binom Lj\le e^{Lh(j/L)}\),
\(\nu_L^{-1}\le C N^{1/4}\), the protected sine-product bound
from W, and (12). There are at most \(N^3\) summands.
A sufficiently small fixed tilt changes their exponents by at
most \(C|z|\). Thus this entire finite complement retains a
fixed exponential gap. No factorial interpolation is used at
the packet endpoints, and no omitted endpoint is declared zero
except where the literal packet (3) is zero.

## 4. A finite rectangle formula retaining every alias and side

We give the contour argument because (14) alone would not justify
continuation of the finite sum.
For a holomorphic function \(f\) on
\(\mathcal R=[a,b]+i[-s,s]\), choose
\(Na,Nb\in\mathbb Z+\tfrac12\).
The literal grid sum inside is
\[
 \sum_{k/N\in(a,b)}f(k/N)
   =\frac1{2\pi i}\int_{\partial\mathcal R}
                   \pi N\cot(\pi Nw)f(w)\,dw.         \tag{15}
\]
There are no other poles. On the upper horizontal side,
\(\pi N\cot(\pi Nw)=-i\pi N+O(Ne^{-2\pi Ns})\);
on the lower side it is
\(+i\pi N+O(Ne^{-2\pi Ns})\).
On a vertical half-grid side its modulus is at most \(\pi N\).
Separate these constants and use Cauchy's theorem to move the two
horizontal integrals of \(f\) to the real segment. Exactly,
\[
       \sum_{k/N\in(a,b)}f(k/N)
                    =N\int_a^b f(t)\,dt+\mathcal R_N f. \tag{16}
\]
The functional \(\mathcal R_N\) is the sum of the two horizontal
remainder integrals and the two retained vertical integrals.
Its horizontal kernels are \(O(Ne^{-2\pi Ns})\); after the
constant-integral moves its vertical kernels are \(O(N)\).
The sign of the main integral is \(+N\): the upper side is
oriented right to left and the lower side left to right.
This construction specifies the connectors rather than dropping
them. The exponentially small horizontal kernels contain every
nonconstant cotangent Fourier mode.

Apply (16) in all three coordinates of the exact interpolant.
The result is the main term
\[
                 N^3\int_{\mathcal B_N} I_N(v;z)\,d^3v \tag{17}
\]
plus all seven nonempty tensor combinations of real integrals
and \(\mathcal R_N\)'s. Here \(\mathcal B_N\) is a real cube
with half-grid sides, within \(O(N^{-1})\) of a fixed cube of
halfwidth \(r\) about \(v_*\). This is an exact identity for the
boxed lattice sum. It retains mixed single-side and multiple-side
terms as well as all corners.

Here is one uniform choice paying those terms. First choose \(r>0\)
small enough that a larger complex cube is in the domain of (14).
For real \(v\) in the cube and \(|y_j|\le s\), holomorphy and the
centered phase give
\[
 \Re\Phi_0(v+iy)
       \le \Re\Phi_0(v)+C(r|y|_1+|y|_1^2).            \tag{18}
\]
The linear bound uses
\(\Im\nabla\Phi_0(v)=\nabla Q_0(v-v_*)=O(r)\).
Take \(r\) small enough that the linear coefficient in (18)
is less than \(\pi/4\) per height, and then choose
\(0<s\ll r\). The real boundary of the cube has a uniform
gap \(g>0\) by (12). Require also
\[
              C(3rs+9s^2)<g/4.                       \tag{19}
\]
All constants can be chosen uniformly over the compact data.

If a tensor boundary term has a vertical side, some real
coordinate is at the cube boundary. Equations (18)--(19)
retain its real gap, even when other coordinates lie on horizontal
or vertical sides. If it has no vertical side, every nonreal
coordinate belongs to a horizontal remainder. Their kernel
contributes \(-2\pi N|y_j|\), which dominates (18) and leaves
at least \(\pi Ns\) whenever a remainder is present.
The unused coordinates are integrated over real segments.
All side lengths and all powers of \(N\) are harmless polynomial
factors. Thus the full seven-term remainder at \(z=0\) is
\[
                  O(e^{N(R(v_*)-\epsilon)})            \tag{20}
\]
for a fixed \(\epsilon>0\), after reducing the gap to absorb
polynomial factors.

Lastly choose the fixed tilt polydisk small enough that its cost
on this entire complex cube is below \(\epsilon/4\).
Since \(\Phi_*(z)=R(v_*)+O(|z|^2)\), reduce it once more so that
the critical-value change has modulus below \(\epsilon/4\).
Then (20) is exponentially relative to the prospective saddle
value for all these complex tilts. The real finite complement
from Section 3 is controlled by the same choice.
No analytic continuation of a real nodal error has been invoked.

## 5. Actual saddle deformation and its oriented coefficient

For small \(z\), set \(q_z=v_z-v_*\). Choose a smooth real cutoff
on \(\mathcal B_N\), equal to one on a smaller central cube and
zero near its boundary. Deform its real chain by
\[
                      v=t+\chi(t)q_z,\qquad
                               t\in\mathcal B_N.       \tag{21}
\]
Multiplying \(q_z\) by a real parameter gives a homotopy with fixed
boundary. It remains in the holomorphic nonzero interpolation
domain. Stokes therefore preserves (17) exactly. Near \(v_z\)
the tangent is the translated real plane. The positive real part
of \(H_0\) persists for small \(z\); its quadratic maximum has a
uniform Gaussian gap. On the cutoff annulus, the original real
gap persists by smallness of \(q_z\). All remaining portions of
this chain, as well as the rectangle terms already estimated,
are exponentially subordinate.

The oriented local Gaussian on this translated plane is
\[
       \int_{\mathbb R^3}e^{-N t^tH_z t/2}\,d^3t
                    =(2\pi/N)^{3/2}/\sqrt{\det H_z}.    \tag{22}
\]
At zero tilt choose the square root by continuously multiplying
the imaginary part of \(H_0\) by a parameter from zero to one.
Its real part stays positive, so the determinant never vanishes.
At parameter zero it is the positive real Gaussian root.
Continue that choice holomorphically in \(z\).
This fixes the orientation and gives coefficient \(+1\).

The factor \(N^3\) in (17), \(N^{-3/2}\) in (14), and
\(N^{-3/2}\) in (22) cancel exactly. This proves (10).
For the relative error, a central range of radius \(N^{-2/5}\)
has the usual Taylor expansion with odd Gaussian terms integrating
to zero. The remaining Gaussian moments and (14) give \(O(N^{-1})\).
Its complement has a Gaussian or a fixed exponential gap.
The argument holds on a larger compact tilt polydisk; Cauchy
estimates give every fixed derivative assertion.

An insertion of any fixed holomorphic function of the occupations
on the protected cube merely multiplies \(a(v_z)\) by its value
there. Its original real finite complement has the same bounds
when the insertion is bounded on the physical support.
Taking the literal clock functions proves (11).
Equivalently,
\[
 \partial_{z_j}\log\mathcal P_N
       =N(v_{z,j}-v_{*,j})+\partial_{z_j}\log
           \!\left((2\pi)^{3/2}a(v_z)/\sqrt{\det H_z}\right)
           +O(N^{-1}).                                \tag{23}
\]
The total-coordinate row is included.

## 6. Original coherent annuli and the scope of the transport

For each of the four head supports choose a fixed radial annulus
containing that entire scaled support with a positive margin.
The endpoints lie strictly between zero and one.
W's original coherent partial resolution is the literal diagonal
matrix
\[
 (W_{p_0})_{aa}
   =N\binom da\int_0^{p_0}t^a(1-t)^{d-a}\,dt
   =\Pr\{\operatorname{Bin}(N,p_0)\ge a+1\}.            \tag{24}
\]
The annulus is \(W_{p_+}-W_{p_-}\).
On each relevant entire packet support its difference from one
is \(O(e^{-cN})\), by the binomial exponential bound proved in W.
Take tensor products on the input and output to obtain
\(W_{\rm in},W_{\rm out}\). All diagonal frames in (7) commute
with these matrices.

Let \(\mathcal P_N[X;z]\) denote (7), and use the same literal
packets and frames for an inserted matrix. Absolute values of
the finite summands are bounded by
\(\operatorname{poly}(N)|\kappa|
e^{N(R(v_*)+C|z|)}\), by (12) and the exact packet bound.
Equations (10) and (24), after a further fixed reduction of the
tilt disk if necessary, therefore give
\[
 \begin{split}
 &|\mathcal P_N[W_{\rm out}X-XW_{\rm in};z]|\\
 &\quad+
 |\mathcal P_N[W_{\rm out}XW_{\rm in}-X;z]|
             \le C e^{-c'N}|\mathcal P_N[X;z]|.         \tag{25}
 \end{split}
\]
These are matrix-element current estimates, not a claim of
operator-norm transport on every complex state.
They concern the original annular coherent matrices and original
finite crossing, with the actual wire frames retained.

The open image of \(z\mapsto v_z\) supplies a concrete sufficient
local membership criterion: every complex occupation triple in
that neighborhood is reached by the specified exact packet
period, including triples with a nonunit total clock. It is not
necessary to reinterpret a noninteger occupation as a physical
matrix index or to change the total-product eigenline section.
The original integer sum itself has been deformed and estimated.

This does not prove that a complete faithful geometric frame lies
in this particular neighborhood. Nor does it prove that the
packets are the actual external states of a fused source, satisfy
the complementary Gauss range and its moving first-normal
condition, or sew around a word. The scalar \(\kappa\), finite
carrier marks, and total-degree weights remain explicit. The
fixed-root theorem is not differentiated in the meridian or in
the quantum parameter; an actual meridian insertion must retain
its own exact matrix formula. No arbitrary geometric knot
coefficient or source lower bound follows from this local period.

## Complete proof directs

* W: notes/research_weighted_reduced_generator_window_transport.md,
  419 lines, SHA256
  800cd02115245208e2f37e688590ad00b0a44b6a274d973cf8c12dd8df6cc2be.
* F: notes/exact_factorial_interpolation_and_complex_contours.md,
  226 lines, SHA256
  1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72.

Only written mathematics and text/hash operations are used.
Frozen and public files are unchanged. Both complete directs
were freshly read nontruncated in this author sequence. The
entire matching final was freshly read back, every used
implication checked, and all three hashes renewed before
author freeze. Independent matching peer and root review
remain separate.
