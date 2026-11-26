# A full-Hermite real-power interpolation of the original crossing

Research note, 3 November 2026. A fixed Gaussian logarithm defines an
exact entire one-parameter group in the original physical algebra.
It agrees with every signed integer crossing power and retains all
first normals. The exact derivative-sampling contour also extends,
with its endpoint current still present.

The resulting parameter equation is explicit. It is not a scalar
transport law for the geometric saddle coefficient. In particular,
its nilpotent-generator contribution is an existing original
twist-period insertion, which can have a strictly larger exponential
rate than the uninserted source. The construction supplies a legitimate
finite family for a continuation argument; it does not supply the
global hypotheses in the
[dominant-saddle transport theorem](research_dominant_saddle_transport.md).

## 1. The specified logarithm and the semigroup

Fix \(N\ge3\), \(D=N-1\), \(\eta=(-1)^D\), and
\[
 \mathcal A_N=\mathbb C[z]/(P_N(z)),\qquad
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f.
 \tag{1}
\]
The distinct double nodes, their angular lifts, and the original
normal coefficients are
\[
 \begin{split}
 c_a&=2\cos((2a+1)\pi/N),&
 \tau_a&=\pi(D-2a)/N>0,\\
 \gamma_a&=\frac{D-2a}{4\sin((2a+1)\pi/N)}
          =\frac{N\tau_a}{4\pi\sin\tau_a},
 &0&\le a<\lfloor N/2\rfloor .
 \end{split}
 \tag{2}
\]
For odd \(N=2m+1\), the additional simple node is
\(c_m=-2,\tau_m=0\). There is no derivative datum at that node.

Set
\[
 \omega_a=\frac{\pi D^2}{4N}+\frac{N\tau_a^2}{4\pi}.
 \tag{3}
\]
Let \(\mathscr G_N\) be the unique degree-\(<N\) real Hermite
polynomial with
\[
 \mathscr G_N(c_a)=\omega_a,\qquad
 \mathscr G_N'(c_a)=\gamma_a
 \quad\hbox{at double nodes},
 \tag{4}
\]
and the prescribed value \(\omega_m\) at the odd simple node.
This fixes the logarithm, not just its exponential.

**Theorem 1.** Define, by the exponential in the finite algebra,
\[
                         R_s=\exp_{\mathcal A_N}(is\mathscr G_N),
                         \qquad s\in\mathbb C.
 \tag{5}
\]
Then \(s\mapsto R_s\) is entire, and
\[
 R_0=1,\qquad R_sR_t=R_{s+t},\qquad R_s^{-1}=R_{-s}.
 \tag{6}
\]
Its full physical data are
\[
 R_s(c_a)=e^{is\omega_a},\qquad
 R_s'(c_a)=is\gamma_a e^{is\omega_a},
 \tag{7}
\]
with only the value at the odd simple node. For every integer \(n\),
this is exactly the original crossing power \(R^n\).

*Proof.* A double-node local factor is
\(\mathbb C[\epsilon]/(\epsilon^2)\). In it the exponential in
(5) is \(e^{is\omega_a}(1+is\gamma_a\epsilon)\).
At the simple node it is the scalar \(e^{is\omega_m}\).
The Chinese remainder decomposition proves (6)--(7) and entireness.
It also shows that their canonical representatives keep every
normal direction.

Write \(q=e^{\pi i/N}\) and
\(\kappa=\exp(\pi iD^2/(2N))\). At integer \(n\),
\[
 e^{in\omega_a}
  =\kappa^n(-1)^{na}q^{na(a+1)},\qquad
 (R^n)'(c_a)/R^n(c_a)=in\gamma_a.
 \tag{8}
\]
These are the original crossing data in
[the source compiler](research_arbitrary_power_source_compilation.md)
and [the full normal calculation](research_all_color_path_normal_bound.md).
Uniqueness of Hermite interpolation therefore proves integer
recovery. \(\square\)

For noninteger \(s\), the expanded phase in (3) contains
\(-\pi sa\), rather than a freely chosen branch of
\((-1)^{sa}\) or a principal numerical power of \(\kappa\).
Equivalently, the fixed entire Gaussian representative is
\[
 C_{N,s}e^{isNt^2/(4\pi)},\qquad
                  C_{N,s}=\exp(\pi isD^2/(4N)).
 \tag{9}
\]
Changing the logarithm by independent integer multiples of \(2\pi\)
at the distinct nodes would give other entire groups agreeing at
integer parameters. Formula (3) excludes that ambiguity. Noninteger
parameters here are an explicitly defined analytic family, not an
assertion that a noninteger crossing is an original topological move.

For real \(s\), every physical value in (7) has modulus one, and
\[
                    |R_s'(c_a)|\le |s|N^2/8.
 \tag{10}
\]
Indeed \(\gamma_a\le N/(4\sin(\pi/N))\le N^2/8\).
Thus all preceding radical-contraction estimates extend uniformly
over compact real-power intervals. The even middle-node derivative
is more sharply bounded by \(|s|N/8\), so the
[contracted midpoint-current estimate](research_bare_kernel_power_three_obstruction.md),
Section 6, extends to real \(s,p\) with the same proof.

One useful finite state norm makes this uniformity explicit:
\[
 \|f\|_{\mathcal H,N}
 =\max\left\{\max_c|f(c)|,\;
        \max_{c_a\ {\rm double}}\frac{|f'(c_a)|}{1+\gamma_a}\right\}.
 \tag{11}
\]
For real \(s\),
\[
 \frac{\|f\|_{\mathcal H,N}}{1+|s|}
      \le\|R_sf\|_{\mathcal H,N}
      \le(1+|s|)\|f\|_{\mathcal H,N}.
 \tag{12}
\]
This follows from the product rule in (7) and then multiplication
by \(R_{-s}\). It controls the whole physical state; it is not a
lower bound for the particular observation \(\phi_N(R_sf)\).

## 2. The original finite trace and its endpoint current

For a polynomial spectator \(f^\sharp(z)\), of arbitrary degree,
write \(f(t)=f^\sharp(-2\cos t)\) and
\[
 \mathcal D_{s,N}[f]=\phi_N(R_sf^\sharp),\qquad
 g_s(t)=\sin t\,f(t)e^{isNt^2/(4\pi)}.
 \tag{13}
\]
Use the full symmetric grid
\(\tau_j=\pi(D-2j)/N\), \(0\le j<N\).
Then, for every complex \(s\),
\[
             \mathcal D_{s,N}[f]
                  =\eta C_{N,s}\sum_{j=0}^{N-1}g_s'(\tau_j).
 \tag{14}
\]
To verify this directly, pair \(\tau_a\) with \(-\tau_a\).
Their two terms are exactly
\(\eta[(4-c_a^2)(R_sf^\sharp)'(c_a)
                 -c_aR_s(c_a)f^\sharp(c_a)]\), by (7).
At the odd simple node the single contribution is
\(C_{N,s}f(0)\), as required. Thus (14) is a full Hermite trace,
not a value-only definition.

The entire oddness \(g_s(-t)=-g_s(t)\) holds for every \(s\).
Consequently the residue proof in
[the exact complete trace contour](research_exact_complete_trace_contour.md),
Proposition 2, gives, for every \(h>0\),
\[
 \begin{split}
 \mathcal D_{s,N}[f]
 ={}&-\frac{N^2C_{N,s}}{\pi i}
    \int_{-\pi-ih}^{\pi-ih}g_s(t)
            \frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}\,dt\\
 &+\frac{\eta N^2C_{N,s}}{\pi}
       \int_{-h}^{h}
          \frac{g_s(\pi+iv)}{4\cosh^2(Nv/2)}\,dv .
 \end{split}
 \tag{15}
\]
There is no new periodicity assumption in this extension: the
proof only uses (14), the grid residues and oddness. The same
argument gives its midpoint-truncated version with the exact
removed-node sum retained. Parameter differentiation under these
finite contours is legitimate.

The Gaussian representative itself is not periodic:
\[
 \frac{C_{N,s}e^{isN(t+2\pi)^2/(4\pi)}}
      {C_{N,s}e^{isNt^2/(4\pi)}}
                  =e^{isN(t+\pi)}.
 \tag{16}
\]
At a physical lift this factor is generally node dependent when
\(s\) is noninteger. Hence one cannot reset the Gaussian logarithm
at the endpoints of a period, or omit the second line of (15).
The canonical polynomial \(R_s(-2\cos t)\) is periodic; (9) is
its specified jet representative on the original logarithmic
window, not a global equality of entire functions.

## 3. The exact parameter equation and its finite-dimensional closure

For any \(s\)-independent original spectator \(f\), differentiation
in the algebra gives
\[
 \frac{d}{ds}(R_sf)=i\mathscr G_N R_sf,\qquad
 \frac{d}{ds}\phi_N(R_sf)=i\phi_N(\mathscr G_NR_sf).
 \tag{17}
\]
This is an exact operator equation, with the explicit solution
\(R_sf=R_{s-s_0}(R_{s_0}f)\).
For a compiled network, the same identity applies in each selected
variable separately, before its original trace. It retains every
free-variable coefficient and ordinary derivative.

Here is its scalar closure. At the double nodes define
\[
 A_a(f)=\eta[(4-c_a^2)f'(c_a)-c_af(c_a)],\qquad
 B_a(f)=\eta(4-c_a^2)\gamma_a f(c_a).
 \tag{18}
\]
The exact original source is the exponential polynomial
\[
 \phi_N(R_sf)=
   \sum_{a<\lfloor N/2\rfloor}e^{is\omega_a}
                   [A_a(f)+isB_a(f)]
   +\mathbf1_{N\ {\rm odd}}e^{is\omega_m}f(-2).
 \tag{19}
\]
All \(\omega_a\) are distinct, and each double-node \(\gamma_a\)
is nonzero. Therefore the minimal polynomial of the multiplication
generator \(\mathscr G_N\) has degree \(N\):
\[
 Q_N(\lambda)=
       \prod_{a<\lfloor N/2\rfloor}(\lambda-\omega_a)^2
       \begin{cases}1,&N\ {\rm even},\\
                \lambda-\omega_m,&N\ {\rm odd}.
       \end{cases}
 \tag{20}
\]
In particular every scalar (19) satisfies
\[
       \prod_{a<\lfloor N/2\rfloor}(\partial_s-i\omega_a)^2
       (\partial_s-i\omega_m)^{\mathbf1_{N\ {\rm odd}}}
                       \phi_N(R_sf)=0.
 \tag{21}
\]
The last factor is omitted at even levels. No constant-coefficient
equation of smaller order works for all original spectators:
otherwise the perfect Frobenius pairing applied at \(s=0\) would
give a polynomial of smaller degree annihilating
\(\mathscr G_N\), contrary to its local Jordan factors.
Special spectators can of course have a smaller equation.

Thus the exact scalar family contains \(O(N)\) physical frequencies,
not an already separated geometric mode. Its modulus can vary
exponentially with \(N\) by coherent cancellation even though
each frequency has unit modulus on the real parameter axis and
the whole-state estimate (12) is uniform.

One can also record the exact moment left after subtracting a
candidate geometric phase. Define \(\mathscr T_N\) by
\[
 \mathscr G_N=\frac{\pi D^2}{4N}\,1+
                                  \frac{N}{4\pi}\mathscr T_N.
 \tag{22}
\]
Its physical values are \(\tau_a^2\), and its double-node
derivatives are \(\tau_a/\sin\tau_a\).
If a chosen geometric branch has angle \(t_*(s)\), then
\[
 \begin{split}
 \left(\partial_s-\frac{iN}{4\pi}t_*(s)^2\right)
       \{C_{N,s}^{-1}\phi_N(R_sf)\}
   =\frac{iN}{4\pi}C_{N,s}^{-1}
             \phi_N(R_s[\mathscr T_N-t_*(s)^2]f).
 \end{split}
 \tag{23}
\]
The inserted factor on the right is not a radical element:
its values \(\tau_a^2-t_*(s)^2\) generally do not vanish.
The earlier bounds for radical edges and midpoint currents
therefore do not control this bulk moment below the desired rate.
Even in a proved one-saddle regime its ordinary transport of the
local amplitude need not have an exponentially smaller rate.

## 4. The nilpotent generator is an actual larger-rate insertion

Let \(\mathscr G_N^{\rm ss}\) have the same physical values
\(\omega_a\) as \(\mathscr G_N\), but zero first normals, and set
\(\mathscr G_N^{\rm rad}=\mathscr G_N-\mathscr G_N^{\rm ss}\).
These definitions use the canonical local-factor decomposition
of the physical algebra. Put
\[
                      U_N=\eta R^{2N}-1.
 \tag{24}
\]
At every double node \(U_N(c_a)=0\) and
\(U_N'(c_a)=2Ni\gamma_a\); its odd simple value is zero.
Thus, exactly in \(\mathcal A_N\),
\[
 (\mathscr G_N^{\rm rad})^2=0,\qquad
 i\mathscr G_N^{\rm rad}=\frac{U_N}{2N},\qquad
 R_s=e^{is\mathscr G_N^{\rm ss}}
                            \left(1+\frac{s}{2N}U_N\right).
 \tag{25}
\]
The parameter equation (17) consequently splits as
\[
 \frac{d}{ds}\phi_N(R_sf)
   =i\phi_N(\mathscr G_N^{\rm ss}R_sf)
                       +\frac1{2N}\phi_N(U_NR_sf).
 \tag{26}
\]
The second term is not generally a lower-rate forcing.

For an explicit original source, take the single selected vertex
with one complete outside edge:
\[
 P_{1,s,N}(0)=\phi_N(R_sK_N(\,\cdot\,,-2)).
 \tag{27}
\]
At the actual integer power \(s=4\), the theorem in
[twist-period insertion growth](research_twist_period_insertion_growth.md),
equation (8) with \(d=1,n=4\), proves
\[
 \frac1{2N}\phi_N(U_NR^4K_N(\,\cdot\,,-2))
   =\frac{i\eta C_{N,4}}{4N(1-4i)^{3/2}}
                      e^{NM_\infty}(1+O(N^{-1})).
 \tag{28}
\]
Its coefficient is nonzero at every sufficiently large level,
at both parities. The same note's Section 4 proves a strict
augmented-rate loss for the uninserted original source:
\[
       |P_{1,4,N}(0)|\le CN^a
                    e^{N(M_\infty-\delta)},\qquad \delta>0.
 \tag{29}
\]
Equations (28)--(29) concern precisely the original kernel, crossing
and trace in (27). They are not a replacement model or an inference
from the size of an isolated physical color. They disprove a general
rule placing the nilpotent term of (26) below the uninserted source
rate. Any successful parameter transport must keep its cancellation
with the other part of the generator, or reorganize the whole
equation without estimating these two terms separately.

The exact cyclic law also persists for the real-power family:
\[
          R_{s+2Nk}=\eta^kR_s(1+kU_N),
                       \qquad s\in\mathbb C,\quad k\in\mathbb Z.
 \tag{30}
\]
It follows from the semigroup and \(R^{2N}=\eta(1+U_N)\).
This is an affine nilpotent correction, not a true full-Hermite
period. The restriction \(k\in\mathbb Z\) in (30) is essential.

## 5. What remains for continuation of the geometric coefficient

The real-power path now has a fixed exact source, fixed normal
conventions, an entire finite parameter dependence, and the original
contour with all endpoint terms. Bounds that use only physical unit
crossing values and polynomial first normals are uniform on compact
real-power intervals, including \([3,64]\).

For the particular internal two-vertex path, the
[uniform pair comparison](research_radical_path_sector_gap.md),
Theorem 5, now gives a positive geometric branch and
\(M_{n,p}>2M_\infty+1/100\) for every real \(n,p\ge3\).
For the interpolated quantum family defined here, both its full
radical contribution and its traced midpoint forcing therefore
have a strict gap below \(M_{n,p}\). The bounds are uniform for
\((n,p)\in[3,64]^2\), since the physical values stay unit and all
normal bounds used above are uniform on that set. A common small
complex outside-boundary neighborhood follows by the polynomial
strip estimates and compactness of the positive geometric branch.
This controls these two actual error sectors along a real-power
path; it does not estimate the whole joint low-sector trace.

What is not supplied is a uniformly controlled one-dimensional
quotient of the actual source cycle, or an equivalent closed equation
for its geometric coefficient with controlled remainder. The exact
bulk insertion in (23) and the larger-rate term in (28) explain
concretely why that conclusion does not follow by differentiating
the finite family. The order-\(N\) equation (21) is a finite-algebra
identity; it is not asserted to quantize a fixed classical
geometric curve. Positive geometry and bounds on selected error
sectors may help construct a transport proof, but do not by
themselves estimate its other cycles or fix its selected coefficient.
