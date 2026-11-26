# A global complementary wire bound for the actual complete cap

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The local cap–vertex attachment has a certified nonzero coefficient.
This note bounds the actual full wire integral outside one short
central interval. It uses the original cap, not its prepared Gaussian.
Negative factorial arguments are retained by their exact reciprocal
reflection formula. The central wire interval and its connecting
contours remain separate.

## 1. Source and statement

Let \(W_N(x,0)\) be the original complete-ended power-three cap in
[the cap theorem](research_homogeneous_wire_complete_cap.md), and put
\[
 Y_h=\frac{\log2}{2\pi},\quad x_h=\frac16+iY_h,\quad
 E=[-1/8,7/50]\ \cup\ [1/5,7/8].
 \tag{1}
\]
The two intervals are the complement of \((.14,.20)\) in a full
wire period. Keep the original corner-deleted vertex
\(\widetilde V_N\) from
[the retained-vertex theorem](research_traced_three_vertex_endpoint.md).

**Theorem 1.** At both parities,
\[
 \sup_{\xi\in E}|W_N(\xi+iY_h,0)|
                      \le CN^A e^{253N/200}.
 \tag{2}
\]
Every fixed ordinary derivative at the complete outside color has
the same exponential bound. On a sufficiently small fixed complex
ordinary-color neighborhood, the exponent in (2) increases by an
arbitrarily prescribed positive constant.

Consequently, if \(\Theta_*\) is the certified action of the
[first actual attachment](research_three_cap_first_attachment.md),
\[
 \left|N\int_{E+iY_h}W_N(x,0)\widetilde V_N(x,x_h)\,dx\right|
 \le N\int_{E+iY_h}|W_N(x,0)\widetilde V_N(x,x_h)|\,|dx|
 \le CN^A e^{N(\Re\Theta_*-1/10000)}.
 \tag{3}
\]
The same strict gap persists for a small complex change of the
outgoing Fourier variable and the ordinary outside color.

Equation (3) concerns the literal complementary portion of the
original wire period with one retained vertex. It does not yet
deform the remaining central interval into the local attachment.

## 2. The physical rows and the change of period representative

Set \(D=N-1\) and \(\eta=(-1)^D\). At a distinct physical root
\(c_a\), \(0\le a\le\lfloor D/2\rfloor\), the exact value of the
continued Newton vector is
\[
 V_a(x)=\frac{(-1)^{D+a}}N
 \prod_{k=1}^{a}2\sin\pi(x+k/N)
 \prod_{k=a+1}^{D}2\sin\pi(x-k/N).
 \tag{4}
\]
At double roots its angular normal is
\[
 H_a(x)=-\tfrac12 V_a(x)
                  \sum_{k=a+1}^{D-a}\cot\pi(k/N-x).
 \tag{5}
\]
These are the full-jet identities of the
[finite Fourier-band theorem](research_newton_interpolation_finite_fourier_band.md).
In particular both jets, and hence the entire cap, have
\(W_N(x+1,0)=\eta W_N(x,0)\). This is an exact quotient identity;
no periodicity of an off-grid Gaussian representative is assumed.

On \(x=\xi+iY_h\), the smooth logarithms of all factors in (4)
have uniform real Riemann-sum errors \(O(1)\). If
\(r=a/N\in[0,1/2]\), their exponent is
\[
 \begin{split}
 \mathcal B(\xi,r)&=\pi Y_h+
  \int_0^r\{f(\xi+v)-f(\xi-v)\}\,dv,\\
 f(v)&=\log|1-\tfrac12e^{2\pi iv}|.
 \end{split}
 \tag{6}
\]
The omitted last mesh interval costs only \(O(1)\). Since
\[
 |1-\tfrac12e^{2\pi i(\xi+v)}|^2
 -|1-\tfrac12e^{2\pi i(\xi-v)}|^2
                 =2\sin(2\pi\xi)\sin(2\pi v),
 \tag{7}
\]
\(\mathcal B\) increases in \(r\) for \(0\le\xi\le1/2\),
and decreases for \(1/2\le\xi\le1\). Thus all physical values
in the latter wire interval have exponent at most \(\pi Y_h\).
The same is true for (5), with polynomial cost, because the fixed
wire height bounds every cotangent. Conversion to ordinary normals
at double roots costs another power of \(N\); the odd simple root
uses only its value.

We shall use negative wire representatives \(-1/8\le\xi\le0\)
for the central angle contour. Their physical rows can instead be
estimated at \(\xi+1\in[7/8,1]\) by exact half-band periodicity.
Their exponent is therefore also at most \(\pi Y_h\).
This choice changes no original physical value or first normal.

## 3. One fixed trace rectangle through the factorial walls

Use
\[
 T=41/20,\qquad H=99/100,\qquad \Lambda=2\pi Y_h=\log2.
 \tag{8}
\]
On the full rectangle \(|\Re t|\le T,-H\le\Im t\le0\),
the original factorial representative is
\[
 B_N(x,t)=
 \frac{N}{G_N(N(1/2-x+t/(2\pi))-1/2)
           G_N(N(1/2-x-t/(2\pi))-1/2)G_N(Nx)^2}.
 \tag{9}
\]
It represents the same full quotient jets for every wire under
consideration, including negative \(\Re x\).

For \(-1/8\le\Re x\le7/8\), both shifted real parts in (9)
stay strictly inside \((-24/25,24/25)\). The reciprocal Gamma
product is holomorphic here: its negative-row divisors are zeros,
not poles. The negative arguments are estimated by the exact identity
\[
 G_N(Nz-1/2)^{-1}
   =\frac{2\cos(\pi Nz)}N\,G_N(-Nz-1/2),
 \tag{10}
\]
with both cosine terms retained. The
[uniform reciprocal-factorial bound](research_uniform_factorial_and_boundary_decay.md)
therefore supplies
\[
 |B_N(x,t)|\le CN^A e^{N\mathfrak b(x,t)},\quad
 \mathfrak b=-\Re J_{\rm side}(1/2-x+t/(2\pi))
             -\Re J_{\rm side}(1/2-x-t/(2\pi))
             -2\Re J_{\rm side}(x).
 \tag{11}
\]
The \(1/(2N)\) shift in the last midpoint factorial has bounded
effect since \(|\Im x|=Y_h>0\). For negative real part,
\[
 J_\pm(z)=-J(-z)\pm i\pi z,\qquad
       \Re J_{\rm side}(z)=-\Re J(-z)-\pi|\Im z|.
 \tag{12}
\]
This is a uniform upper bound across a factorial zero, with no
discarded reflection term or wall residue.

The chosen rectangle also lies in a compact subset of
\(\Re(-2\cos t)<2\), since
\(-2\cos T\cosh H<3/2\). The literal low complete kernel therefore
has the all-parity bound
\[
 |\mathcal L_N(-2\cos t)|\le CN^A e^{N\Re\Psi(t)},\qquad
 \Psi(t)=-4J(1/4+t/(4\pi))-4J(1/4-t/(4\pi)),
 \tag{13}
\]
by the actual last-row normalization and the low-kernel interpolation
theorem used in the cap proof. This concerns the exact low kernel;
the removed outside radical is estimated separately below.

Apply the original full-Hermite trace contour at midpoint cuts
\(T_N=T+O(N^{-1})\). Its lower horizontal contribution has the
same density as (15) of the cap theorem. Its exponential upper
rate, including the original primary double-pole trace weight, is
\[
 \mathcal R(x,\tau,h)=
 \mathfrak b(x,\tau-ih)+\Re\Psi(\tau-ih)
                         +\frac{3\tau h}{2\pi}-h.
 \tag{14}
\]
On the lower horizontal set \(h=H\). On the folded verticals set
\(\tau=\pm T\), \(0\le h\le H\).
The exact midpoint denominator is \((1+e^{-Nh})^2\), so (14)
bounds every vertical current, including its \(h=0\) endpoint.
Both angular signs and the odd simple node are retained by this
original contour identity. No claim that its off-grid integrand
is periodic in \(t\) is used.

The outward certificate in Section 5 proves
\[
 \mathcal R(\xi+iY_h,\tau,H)<253/200
 \quad (|\tau|\le T,\ \xi\in E),
 \qquad
 \mathcal R(\xi+iY_h,\pm T,h)<253/200
 \quad (0\le h\le H,\ \xi\in E).
 \tag{15}
\]
It splits the vertical heights at \(h=\Lambda\), retaining the
change of factorial side there. At a zero shifted argument the
continuous upper exponent is used, not a logarithmic branch reset.
Strictness on these compact domains also handles all midpoint
perturbations.

## 4. Omitted original rows, radicals and the exterior wire integral

For \(0\le\xi\le1/2\), (6)--(7) show that physical rows with
\(|t|\ge T_N\) have \(B_N\)-exponent at most
\(\mathfrak b(\xi+iY_h,T)\), up to the usual polynomial factor.
The old real complete-kernel tail bound and its first normals
have rate \(\Psi(T)\). The certificate also checks
\[
 \mathfrak b(\xi+iY_h,T)+\Psi(T)<253/200
 \quad\text{on}\quad [0,7/50]\cup[1/5,1/2].
 \tag{16}
\]
For the remaining wire intervals use the high-period physical bound
following (7):
\[
                   \Psi(T)+\pi Y_h<23/20<253/200.
 \tag{17}
\]
Thus every omitted physical value and original first-normal term
has the desired bound.

The removed outside-radical kernel has polynomial physical values
and normals. The maximum physical \(B_N\)-exponent on the positive
half period is at the complete trace angle and then at
\(\xi=1/4\): differentiation gives
\(\partial_\xi\Re b(x,0)=2\log|\cot\pi x|\).
The certificate checks
\[
 \mathfrak b(1/4+iY_h,0)<2/3,\qquad \pi Y_h<2/3.
 \tag{18}
\]
Consequently the entire removed radical trace has rate at most
\(2/3\). Ordinary crossing normals cost only powers of \(N\).
Together (15)--(18) prove (2), with every original finite term
accounted for. The existing low-kernel bound with a small complex
ordinary outside color adds only its angular-height cost; the
physical row/normal estimates have the same property. These costs
can be made arbitrarily small. Evenness gives ordinary-color
continuation at the complete ramified point, and Cauchy's estimate
gives the fixed higher normals.

The [global retained-wire theorem](research_three_vertex_global_wire_bound.md)
gives \(|\widetilde V_N(\xi+iY_h,x_h)|\le CN^A e^{2cN}\)
on the entire period, where \(c=2J(5/6)\).
The two factors have the same half-band sign under \(x\mapsto x+1\),
so their product is a literal period-one integrand. The first
attachment certificate gives \(\Re\Theta_*>19113/10000\).
The scalar certificate here gives
\[
 c<161533/500000,\qquad
 \frac{19113}{10000}
  -\left(\frac{253}{200}+2\frac{161533}{500000}\right)
                 >\frac1{10000}.
 \tag{19}
\]
Integration of the absolute value proves (3). A sufficiently small
complex perturbation of the fixed output and ordinary boundary
preserves this reserve: the retained finite-product exponents vary
uniformly on their compact index domain, while the free-outside
low-kernel and physical-row bounds used above add an arbitrarily
small angular-height cost. This proves the theorem. \(\square\)

## 5. Reproducible compact certificate

The [author](../experiments/certify_three_cap_wire_complement.py)
and [artifact](../repro/results/research-three-cap-wire-complement.json)
cover all domains in (15)--(16). The wire intervals are
\([-1/8,0],[0,7/50],[1/5,1/2],[1/2,7/8]\).
For each, the six two-dimensional contour domains are the two
bottom angular halves, and the positive/negative verticals on
\(0\le h\le\Lambda\) and \(\Lambda\le h\le H\).
There are two further one-dimensional physical-tail domains.
All coordinates are affine functions of closed rational boxes in
\([0,1]^2\), with the exact constants \(\pi,\log2\) evaluated by Arb.

The real primitive is computed on its actual side. Equivalently,
for \(z=a+ib\), its real part is the real part of
\[
 -\frac{i\pi}{2}(w^2-w)
 +\frac{i}{2\pi}\operatorname{Li}_2(e^{2\pi iw})-\frac{i\pi}{12},
                         \qquad w=a+i|b|.
 \tag{20}
\]
For a box meeting \(z=0\), a direct elementary bound avoids a
singular logarithm. If \(|z|\le1/20\) in either closed side,
\[
 |J_{\rm side}(z)|
 \le \frac1{20}\left\{-\log(\pi/10)+\pi+1+\frac1{199}\right\}
 <3/10.
 \tag{21}
\]
Indeed \(|\sin(\pi z)/(\pi z)-1|<1/200\), so its logarithm has
modulus at most \(1/199\). Integrate
\(\log(2\pi z)+\log(\sin(\pi z)/(\pi z))\) radially, with
\(|\arg z|\le\pi\). The function \(-r\log(2\pi r)\) is increasing
up to \(r=1/20\). This proves (21), including the limiting value
at zero. It is used only for boxes meeting zero, and only as an
upper/lower enclosure, not as an asymptotic.

Every accepted cell stores its rational binary partition path.
The [independent replayer](../experiments/replay_three_cap_wire_complement.py)
checks exact coverage and re-evaluates each cell at higher precision,
using (12) to reflect negative real parts into the ordinary positive
strip. It imports no author code. The
[replay record](../repro/results/research-three-cap-wire-complement-replay.json)
retains the artifact hash and all scalar comparisons.

The statement remains an exterior-wire bound. A full first-attachment
theorem additionally needs the central interval \([.14,.20]\) and
the index and trace currents created in its deformation. The following
section supplies its two vertical wire connections.

## 6. The two vertical joins to the actual stationary height

Let \(x_c\) be the certified first-attachment root and put
\(h_c=\Im x_c\). Its certified disk gives
\[
 \frac{1013}{10000}<h_c<Y_h,
 \qquad 0<Y_h-h_c<\frac9{1000}.
 \tag{22}
\]
Define the two oriented vertical segments with real parts \(7/50\)
and \(1/5\), joining height \(Y_h\) to \(h_c\).

**Proposition 2.** On the slightly larger height interval
\(1013/10000\le h\le Y_h\), the actual complete cap satisfies
\[
 \begin{split}
 |W_N(7/50+ih,0)|&\le CN^A e^{1261N/1000},\\
 |W_N(1/5+ih,0)|&\le CN^A e^{6319N/5000}.
 \end{split}
 \tag{23}
\]
Consequently the absolute integral of
\(N W_N(x,0)\widetilde V_N(x,x_h)\) over either vertical join is
\[
 O\!\left(N^A e^{N(\Re\Theta_*-1/20000)}\right).
 \tag{24}
\]
Both parities and every fixed ordinary outside normal are retained.
The bound persists on a sufficiently small complex neighborhood of
the complete outside color and fixed outgoing wire.

*Proof.* Use exactly the original trace representation from Sections
1--3, with \(T=41/20\) and depth \(99/100\). Formula (14) now has
the variable wire height \(h\). The complete low-kernel half-plane
bound still holds, since it depends on the trace rectangle, and the
factorial side formula is unchanged. Split the folded verticals at
the moving value \(2\pi h\); this keeps every negative-real factorial
argument on its original side. The physical tails are bounded by
\(\mathfrak b(x,T)+\Psi(T)\), and the radical trace by
\(\mathfrak b(x,0)<2/3\). Their original full normals have the same
polynomial costs as above.

There is a useful exact reduction on the positive central bottom,
\(0\le\Re t\le9/5\). The actual cap phase in
[the joint concavity lemma](research_three_vertex_joint_concavity.md#3-adding-the-actual-complete-cap-phase)
satisfies \(-\Re\mathcal F_{3,xx}>0\) throughout this wire-height
interval at trace depth \(99/100\). Holomorphy therefore gives
\[
 \partial_h^2\Re\mathcal F_3(\xi+ih,t)
          =-\Re\mathcal F_{3,xx}(\xi+ih,t)>0.
 \tag{25}
\]
Its maximum over the wire-height interval occurs at an endpoint.
Thus this part needs only four one-dimensional comparisons, one
for each wire side and height endpoint. The remaining positive
bottom \([9/5,T]\), the negative bottom, and all folded verticals
are checked on their full two-dimensional domains. The two physical
tails and radical observations are one-dimensional. These are exactly
the twenty domains of the
[outward certificate](../experiments/certify_three_cap_wire_joins.py)
and its [saved cover](../repro/results/research-three-cap-wire-joins.json).
They prove (23); no sampled maximum is used.

The [one-height retained bound](research_three_vertex_global_wire_bound.md#6-a-quantitative-one-height-bound-for-the-first-attachment-joins)
applies on the actual joins by (22), and gives rate below \(6474/10000\).
The certified attachment action then gives
\[
 \Re\Theta_*>\frac{19113}{10000},\qquad
 \frac{19113}{10000}-\frac{6319}{5000}-\frac{6474}{10000}
                       =\frac1{10000}>\frac1{20000}.
 \tag{26}
\]
This proves (24), including the wire measure factor \(N\), which is
polynomial. The exact finite cap and retained vertex are holomorphic
in the positive-height strip of these joins; these are ordinary
wire contour connections, with no unrecorded trace variation term.
The ordinary-normal and small outside-neighborhood assertions use
the same full low-kernel and physical-row estimates as Theorem 1.
The retained finite-product bound varies continuously on its compact
index domain. Their strict reserve pays the stated small perturbations.
\(\square\)

The [independent join replayer](../experiments/replay_three_cap_wire_joins.py)
checks every rational binary partition and uses the reflection-based
primitive from the exterior replay. Its
[record](../repro/results/research-three-cap-wire-joins-replay.json)
retains the full cover and dependency hashes. The first brute-force
two-dimensional attempt exhausted its visit budget without saving a
certificate; (25) is the mathematical reduction used by the completed
certificate. No failed attempt is treated as evidence for the bound.

The central horizontal trace/index assembly remains separate from
Proposition 2. In particular (24) does not discard its index sides,
cotangent aliases or angular currents.

