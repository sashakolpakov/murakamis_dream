# A positive tree where absolute physical cut norms lose exponentially

Private written proof, 15 November 2026.

The full positive geometric action need not exceed the sum of the
complete rates of the pieces left by a radical matching. This already
fails for an original zero-power component whose exact source is
controlled by the existing positive Newton theorem. In the same
component, even taking absolute values only after retaining the full
physical Gram matrix loses a fixed exponential amount. The actual
radical term has a strict gap; its physical-color absolute expansion
does not. Thus the obstruction concerns the proposed estimate, not the
zero-power volume theorem or a coherent treatment of general powers.

## 1. Original component and its positive primitive point

Take an original circle tree with two adjacent selected vertices
\(v,w\), each of degree four. Each has three distinct outside
neighbors. Set both selected crossing powers to zero and all six
outside angles to zero. The selected component has seven incident
edges. All degrees refer to the original tree, and all edge constants
and unit primitive charges are retained.

Let \(\alpha\) be the unique solution in \((0,\pi/4)\) of
\[
 3\alpha+\arcsin(\tan\alpha)=\pi,
 \qquad \beta=\arcsin(\tan\alpha),\qquad
 H=2\operatorname{artanh}(\sin\alpha).
 \tag{1}
\]
Existence and uniqueness follow from strict increase: the left side
has endpoint values zero and \(5\pi/4\). In particular
\(0<\beta<\pi/2\). Put
\[
                         t_v=t_w=-iH.
 \tag{2}
\]

The original meridian increment on an edge is
\[
 r_t=\operatorname{arsinh}\bigl(\tan(t/2)\cos(u/2)\bigr).
 \tag{3}
\]
At an outside edge its selected return is \(-i\alpha\) and its
outside return is zero. At the middle edge both returns are
\(-i\beta\). Indeed \(\tan(-iH/2)=-i\sin\alpha\) and
\(\cos(-iH/2)=1/\cos\alpha\). The principal inverse sine
values remain strictly below \(\pi/2\), so these are the original
branches continued from completeness. Equation (1) therefore gives
\(P_v=P_w=-\pi i\), exactly the unit primitive equations at
power zero.

This is a positive original edge configuration, not merely a solution
of the exponentiated equations. In the original rational coordinates
\(a=\tan(t/2),b=\tan(u/2),q^2=1+a^2+b^2\), the outside edges
have \(q=\cos\alpha>0\), while the middle edge has
\[
                     q=\sqrt{1-2\sin^2\alpha}>0.
 \tag{4}
\]
Both \(a,b\) have zero real part. Hence
\(\Re q>\sqrt{(\Re a)^2+(\Re b)^2}\), which is exactly
positivity of all eight original tetrahedra on each edge.

## 2. Its energy exceeds the complete connecting-edge budget

Write \(E(A,y)\) for the square energy normalized by \(E(0,0)=0\),
with
\[
 E_A=\tfrac12\operatorname{arsinh}(\tan(2A)\cos(2y)),\qquad
 E_y=\tfrac12\operatorname{arsinh}(\tan(2y)\cos(2A)).
 \tag{5}
\]
At (2), all real angles are zero. Each outside edge has its two
square coordinates \((0,-\alpha/2)\), up to the separate even
symmetries of \(E\). The middle edge has two copies of
\((\beta/2,\beta/2)\), up to those symmetries. Consequently its
original total energy is exactly
\[
 \mathcal E_* =48E(0,\alpha/2)+8E(\beta/2,\beta/2).
 \tag{6}
\]
The positive primitive point is the unique convex minimum. No other
coordinates have been frozen in computing this minimum.

For \(0\le y,t\le\pi/4\), continuity at the endpoints and (5)
give the elementary bounds
\[
 E(0,y)\ge y^2/2,\qquad
 E(t,t)\ge\frac{2\operatorname{arsinh}1}{\pi}t^2.
 \tag{7}
\]
For the first, \(\operatorname{arsinh}(\tan u)\ge u\) on
\([0,\pi/2)\), since its derivative is \(\sec u\ge1\).
For the second,
\[
 \frac{d}{dt}E(t,t)=\operatorname{arsinh}(\sin2t).
\]
This last function is concave and increasing on \([0,\pi/4]\).
It lies above the chord from zero to \(\operatorname{arsinh}1\);
integration gives (7).

Weighted Cauchy--Schwarz, with \(3\alpha+\beta=\pi\), now yields
\[
 \mathcal E_*
 \ge6\alpha^2+\frac{4\operatorname{arsinh}1}{\pi}\beta^2
 \ge\frac{\pi^2}{3/2+\pi/(4\operatorname{arsinh}1)}>4.
 \tag{8}
\]
The last inequality has an elementary rational verification.
The tangent bound \((1+x^2)^{-1/2}>1-x^2/2\) for \(x>0\)
implies \(\operatorname{arsinh}1>5/6\). Thus the denominator
in (8) is less than \(3/2+3\pi/10\). The classical bound
\(\pi>25/8\) and monotonicity of \(x^2-6x/5-6\) for
\(x>3/5\) give
\[
 \pi^2-6\pi/5-6>
 (25/8)^2-6(25/8)/5-6=1/64>0.
\]

Let \(G=\sum_{j\ge0}(-1)^j/(2j+1)^2\) and
\(M_\infty=4G/\pi\). The alternating series gives \(G<1\).
The calibrated original action-energy identity therefore gives
\[
 M=7M_\infty-\mathcal E_*/\pi,
 \qquad
 \boxed{\quad 6M_\infty-M>
                    \frac{4-4G}{\pi}>0.\quad}
 \tag{9}
\]
Cutting the middle edge and replacing its two endpoint traces by
physical evaluations leaves two untraced three-edge stars. They are
not six independent components: each star retains its shared center
color. Completing their boundary angles gives total classical rate
\(6M_\infty\). Thus the proposed strict comparison of the full
rate with these complete component rates is false.

## 3. The exact original radical and its absolute physical expansion

Let \(N\ge3\), set \(D=N-1\), \(m=\lfloor N/2\rfloor\), and retain
\[
 \begin{gathered}
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(f)=(-1)^D N^2[z^D]\operatorname{rem}_{P_N}f,\\
 s_j=2\sin(j\pi/N),\quad S_j=\prod_{h=1}^j s_h,\quad S_0=1,\quad
 c_a=2\cos((2a+1)\pi/N),\\
 e_j(z)=S_j^{-2}\prod_{h<j}(c_h-z),\qquad
 \mathsf K_N(z,w)=\sum_{j=0}^{D}e_j(z)e_j(w).
 \end{gathered}
 \tag{10}
\]
The double roots have \(0\le a<m\); the odd simple root is
retained in \(P_N\). Put
\[
 B_N(z)=\mathsf K_N(z,-2),\quad f_N(z)=B_N(z)^3,\quad
 \operatorname{rem}_{P_N}f_N=\sum_{r=0}^{D}f_{N,r}e_r.
 \tag{11}
\]
There are no crossing or framing factors to remove, since both
selected powers are zero. The original complete source is
\[
 Z_N=(\phi_N\otimes\phi_N)
          [\mathsf K_N(z,w)f_N(z)f_N(w)]
                         =\sum_{r=0}^{D}f_{N,r}^{2}.
 \tag{12}
\]
This follows from the exact complementary pairing
\(\phi_N(e_i e_j)=\mathbf1_{i+j=D}\).

On the middle edge retain its whole high radical
\(\sum_{r<m}e_{D-r}\otimes e_{D-r}\). Its contracted term is
\[
 T_N=\sum_{r=0}^{m-1}f_{N,r}^{2}
     =\sum_{a,b=0}^{m-1}W_{ab}f_N(c_a)f_N(c_b),
 \tag{13}
\]
where the literal physical Gram matrix is
\[
 \begin{aligned}
 b_{ra}&=(-1)^{r+a}
       \frac{s_{2a+1}S_r^2}{S_{r-a}S_{r+a+1}}\quad(a\le r),\\
 W_{ab}&=\sum_{r=\max(a,b)}^{m-1}b_{ra}b_{rb}.
 \end{aligned}
 \tag{14}
\]
All full first normals are included in this identity. The known exact
bounds are \(|b_{ra}|\le2\), \(|W_{ab}|\le4m\), and
\(\operatorname{sign}W_{ab}=(-1)^{a+b}\).
The numbers \(f_{N,r}\) are real. Moreover
\(f_{N,0}=f_N(c_0)=1\), because
\(\mathsf K_N(c_0,-2)=1\). Hence
\[
                              T_N\ge1.
 \tag{15}
\]
The squares in (13) are squares of coefficients of the canonical
remainder of \(f_N\); they are not coefficients of \(f_N^2\).

Define the absolute physical-color expansion, retaining every Gram
entry and each star's shared boundary color, by
\[
              A_N=\sum_{a,b<m}|W_{ab}|f_N(c_a)f_N(c_b).
 \tag{16}
\]
Every value \(f_N(c_a)\) is positive.

**Proposition.** At both level parities,
\[
                        \log A_N=6NM_\infty+O(\log N).
 \tag{17}
\]

**Proof.** The original low Newton products obey, uniformly for
\(0\le j\le D-m\),
\[
 \log e_j(-2)=N g(j/N)+O(\log N),\qquad
 g(x)=J(2x)-4J(x),\quad
 J(x)=\int_0^x\log(2\sin\pi u)\,du.
 \tag{18}
\]
This is the sine-factorial/midpoint product estimate for the actual
complete leaves, explicitly recorded in (11) of the internal-high
source theorem. Its uniform logarithmic error follows by isolating
the endpoint logarithmic singularities in the Riemann sums. The
original half-step in \(c_h\) changes that error, not the profile.
One has
\[
 g'(x)=2\log\cot(\pi x),\qquad
 \max_{[0,1/2]}g=g(1/4)=2G/\pi=M_\infty/2.
 \tag{19}
\]
Here \(J(1/2)=0\) and \(J(1/4)=-G/(2\pi)\), as in the
original sine-factorial profile.

At a double node \(c_a\), \(e_j(c_a)>0\) for \(j\le a\)
and equals zero for \(j>a\). For \(j\le a<m\), comparison of
each defining factor also gives \(e_j(c_a)\le e_j(-2)\).
Thus (18)--(19) show uniformly in \(a\)
\[
 0<B_N(c_a)\le\sum_{j\le a}e_j(-2)^2
                         \le e^{NM_\infty+O(\log N)}.
 \tag{20}
\]
The polynomial Gram bound and polynomial number of terms prove the
upper bound in (17).

For the lower bound take \(a=m-1\), the last double node.
Then \(c_a+2=O(N^{-2})\). Choose \(j=\lfloor N/4\rfloor\).
For large \(N\), \(j\le a\) and all \(c_h+2\), \(h<j\),
are bounded below by a positive constant. Therefore
\[
 \frac{e_j(c_a)}{e_j(-2)}
    =\prod_{h<j}\left(1-\frac{c_a+2}{c_h+2}\right)
                         =\exp(O(N^{-1})).
 \tag{21}
\]
The one positive summand with this \(j\) in \(B_N(c_a)\)
has rate \(M_\infty\), so (20) is sharp at that node.
The Gram diagonal has \(W_{aa}\ge b_{aa}^2\), and exact factorial
reflection gives
\[
 b_{aa}=\frac{S_a^2}{S_{2a}}=
 \begin{cases}
 s_1/2,&N=2m,\\[1mm]
 s_1s_2/s_m^2,&N=2m+1.
 \end{cases}
 \tag{22}
\]
Thus \(b_{aa}\) is bounded below by a fixed inverse power of
\(N\) at both parities. The single positive diagonal summand
\(W_{aa}B_N(c_a)^6\) in (16) proves the lower bound in (17).
\(\square\)

In particular no estimate obtained by taking absolute values termwise
in this exact physical Gram expansion can have rate below \(M\).
Keeping joint absolute Gram weights is insufficient; their signs must
still participate in the calculation.

## 4. The coherent radical is nevertheless smaller

The existing zero-subtree theorems apply to this very source. Their
regularity condition at the middle edge is satisfied because
\[
            \sinh(H/2)^2=\tan^2\alpha<1.
 \tag{23}
\]
The internal-high theorem gives a strict gap below \(M\) when
the six boundary indices are low. Its identification of the positive
Newton maximum with \(M\) retains the original primitive action.

Here the low-boundary restriction is exact for the radical term.
For \(r<m\), the same original divided-difference identity gives
\[
 f_{N,r}=\sum_{a=0}^{r}b_{ra}
       \left(\sum_{j=0}^{a}e_j(c_a)e_j(-2)\right)^3.
 \tag{23a}
\]
Only boundary indices \(j\le r<m\) occur. Replacing every
\(B_N\) by its low part \(\sum_{2j<N}e_j(-2)e_j\)
therefore leaves \(T_N\) unchanged, at both parities. Equivalently,
the positive Newton multiplication support never lowers an output
index below an input index. All high-boundary sectors vanish exactly
in this radical term; no bound for them is needed.

Thus \(T_N\) is literally the internal-high term of the source
with low boundary leaves. The internal-high theorem alone supplies
some \(\varepsilon>0\) and fixed \(C,q\) such that
\[
                 1\le T_N\le C N^q e^{N(M-\varepsilon)}
 \tag{24}
\]
for all sufficiently large levels of either parity. This imports the
already proved coherent zero-source bounds; it is not deduced from
(17), from positivity of \(W\), or from the classical energy alone.

Combining (9), (17), and (24) quantifies the lost cancellation:
\[
 \liminf_{N\to\infty}\frac1N\log\frac{A_N}{T_N}
 \ge6M_\infty-M+\varepsilon
 >\frac{4-4G}{\pi}+\varepsilon>0.
 \tag{25}
\]
We do not assert an exact exponential rate or a leading asymptotic
for \(T_N\). The lower bound one is used only to make the ratio
well defined. The useful identity is instead
\[
 T_N=\sum_{r<m}
          \left(\sum_{a\le r}b_{ra}B_N(c_a)^3\right)^2.
 \tag{26}
\]
The signed divided differences inside these squares recover the
original Newton coefficients before their positive pairing.
They cannot be replaced by independent physical-value suprema.

## 5. Consequence for the general strategy

This fixed positive original component disproves a universal strict
comparison based only on complete cut-component rates or on absolute
physical Gram weights. It does not disprove the exact matching
identity, a coherent cut estimate, or stability under arbitrary short
fillings. The zero component itself is already solved by its positive
Newton source theorem.

For general signed powers, a successful estimate must retain enough
of the divided-difference cancellation, Newton coefficient support,
or an equivalent coherent source calculation. The compact classical
descent contour does not supply that cancellation by itself. This
note proposes no unproved replacement estimate and asserts no new
geometric-cycle or scalar lower bound for arbitrary short sources.

## Pinned direct sources

* `notes/research_positive_period_inverse_descent.md`, SHA256
  `b9b5c3d61c704700e9431315cf50591c921ebeb95becdf6a52877606bdbc4565`:
  calibrated original action-energy identity and variational minimum.
* `notes/research_positive_edge_global_monotonicity.md`, SHA256
  `da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500`:
  actual meridian increments, positive branches and shape criterion.
* `notes/research_positive_filling_convex_variation.md`, SHA256
  `2777b2bcb149d64a79757ba64ccb16be5438cf37ce820ad50c5f532afd8fc6c0`:
  the square energy, even symmetries and original square coordinates.
* `notes/research_high_newton_radical_contraction.md`, SHA256
  `1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03`:
  exact full-Hermite radical contraction, physical Gram coefficients,
  polynomial coefficient bounds and sine-factorial normalization.
* `notes/research_zero_subtree_internal_high_gap.md`, SHA256
  `1a2edaa55af545613c20a60158f2cb314bb86c1254f7c53e6cb56a42f5b5f5fa`:
  regular internal-high gap and equality of its rate with the original
  primitive action, and the complete low-leaf factorial profile.

Only written proofs and source-text reads enter this note. No
mathematical code, numerical calculation, test or compilation was run.
Frozen manuscripts and other notes were not edited.
