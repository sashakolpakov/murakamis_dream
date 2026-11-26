# Typed last-row boundary design and target envelopes

Research design, 5 November 2026. This specifies the finite boundary
family for the two [typed reference domains](research_mixed_typed_last_row_envelopes.md)
and a sharper target-envelope acceptance bound. No sign on that
family is asserted, and no full run is proposed here. The only
proposed pilot is the low-height subset in Section 4.

## 1. Complete boundary generators and case count

Write \(C_3,C_4\) for the original reduced circles, each
parametrized once by \(c_n+r_ne^{2\pi it}\), \(0\le t\le1\).
On a circle keep only points satisfying every defining clipping
inequality of \(K_n\). The straight generators are as follows;
each row is the closed segment between its two displayed endpoints.

| Type and generator | Endpoints |
|---|---|
| \(H_3^-\) | \(7/20-\sqrt{3045}/1000-9i/125\), \(49/125-9i/125\) |
| \(H_3^+\) | \(7/20\pm\sqrt{805}/1000+17i/250\) |
| \(S_3\) | \(49/125-9i/125\), \(x_*+ih_*\) |
| \(H_4^-\) | \(3/10\pm\sqrt{29}/250-27i/250\) |
| \(H_4^+\) | \(3/10\pm\sqrt{999}/1000-i/1000\) |

Here the slanted circle intersection is exactly
\[
 h_*=-\frac{49}{625}+\frac{\sqrt{16906}}{10000},\qquad
 x_*=\frac{233}{625}+\frac{3\sqrt{16906}}{10000}.
 \tag{1}
\]
Its other line-circle intersection lies below the permitted height
strip. The lower type-three chord ends at its intersection with
\(x-3h=76/125\), not at the excluded right circle intersection.
The typed-domain proof verifies these facts and all closed endpoints.

Thus the generator lists are
\[
 \mathcal G_3=(C_3,H_3^-,H_3^+,S_3),\qquad
 \mathcal G_4=(C_4,H_4^-,H_4^+).
 \tag{2}
\]
The circle entries stand for all their admitted portions, using
strict exclusion masks. They are not an assertion that each circle
portion is connected. Together with the straight segments they
cover the entire boundary, including every intersection and every
endpoint; duplicated descriptions of an endpoint are harmless.

For a chosen boundary generator, parameterize the other input by
its full reduced disk, \(c_n+r_n\rho e^{2\pi i\theta}\),
\(0\le\rho,\theta\le1\), and impose its typed clipping
constraints. This gives three real parameters. Reject a box only
if its entire input enclosure strictly violates a constraint:
the lower or upper height bound, or, for type three,
\(\Re z-3\Im z\le76/125\). A boundary-straddling or
undecidable box remains. Full circles and disks are inside their
old source domains before these masks are imposed.

There are 42 generator cases if both boundary slots are listed
literally. Exact local symmetry reduces this to **28**. Indeed
the original two-leg equations swap their roots when the two
external inputs are swapped. On \(K_n\times K_n\), this
exchanges the boundary slots and the two conditional orientations.
Since both orientations are tested, only boundary slot zero is
needed for a homotyped product. This is local map symmetry, not
reflection of a word or of a finite matrix coefficient.

For each own flag \(\epsilon=0,1\), the complete case list is:

| External types | Boundary slot and generators | Cases per own flag |
|---|---|---:|
| \((3,3)\) | Slot 0, every generator in \(\mathcal G_3\) | 4 |
| \((3,4)\) | Slot 0 with \(\mathcal G_3\), and slot 1 with \(\mathcal G_4\) | 7 |
| \((4,4)\) | Slot 0, every generator in \(\mathcal G_4\) | 3 |

The mixed case retains both slots. Its two boundary types are not
identified by the homotyped symmetry. The two own flags give
\(2(4+7+3)=28\) cases. These remain sufficient auxiliary
domains; actual open words need not realize their independent points.

## 2. Original allocation and separable target maximization

For one orientation write \((s;A,B)\), where \(B\) is the
other output of the same original two-leg map. Let \(\eta\)
be the type-four flag of the first external input and \(\epsilon\)
the own flag. With \(Z=(A,B)=U+iH\), retain
\[
 \begin{split}
 \phi(Z)&=Q_\epsilon(s;A,B)
             -(1+\eta/2)g(A)-(1+\epsilon/2)g(B),\qquad P=\phi',\\
 R_{vw}(X,H)&=-2\pi vH_1+2\pi wH_2
             -\frac\eta2G_{H_1}(X_1)-\frac\epsilon2G_{H_2}(X_2),\\
 D_{vw}(Z,X)&=R_{vw}(X,H)-\Re\phi(Z)
                -\Re P(Z)\mathbin{\cdot}(X-U)
                +\kappa_0\|X-U\|^2,\quad
        \kappa_0=1/2500000.
 \end{split}
 \tag{3}
\]
Here \(G_h(x)=\Re g(x+ih)\), \(X\in I^2\),
\(I=[11/50,9/20]\), and all four \(v,w\in\{0,1\}\)
are retained. The right external type influences the reference
domain and root map; it does not replace \(\epsilon\) in (3).

For a target coordinate with allocation flag \(\tau=0\),
the deficit is convex in that coordinate. Its maximum is at an
endpoint of \(I\). For \(\tau=1\), its target slope is
\[
 b(x;Z)=-\tfrac12\Re g'(x+iH_i)-\Re P_i
                   +2\kappa_0(x-U_i),\qquad
 \partial_x b<-\frac{9\pi}{140}+2\kappa_0<-c_0,
 \quad c_0=1/5.
 \tag{4}
\]
Thus it has a unique clipped maximizer. The two target terms in
(3) are separable, and the carrier is independent of both targets.
Each weighted optimizer is consequently independent of \((v,w)\)
and of the other target coordinate. Compute its enclosure only
once per orientation and parameter box.

Fix the endpoint choices of all unweighted coordinates. The number
of carrier/endpoint envelopes per box, including both orientations,
is then:

| Own flag | External \((3,3)\) | External \((3,4)\) | External \((4,4)\) |
|---|---:|---:|---:|
| \(\epsilon=0\) | 32 | 24 | 16 |
| \(\epsilon=1\) | 16 | 12 | 8 |

These counts retain every branch. They permit reuse of the original
root enclosure, its response, the critical value and marginals,
the conditional Hessian, and the weighted optimizer data. No
separate root solve is needed for a carrier or target choice.

## 3. Target envelopes with a midpoint-only gain

Choose rational target trials \(r_i\in I\) for the weighted
coordinates. Suppose a whole parameter box gives
\(b(r_i;Z)\in[\beta_i^-,\beta_i^+]\). Strong monotonicity
in (4) encloses every true clipped optimizer in
\[
 J_i=I\cap
 \left[r_i+\frac{\min(0,\beta_i^-)}{c_0},
       r_i+\frac{\max(0,\beta_i^+)}{c_0}\right].
 \tag{5}
\]
For example, a positive slope moves the optimizer rightward by
at most \(b(r_i;Z)/c_0\). A clipped right endpoint is also
contained, because a positive slope there implies at least
\(c_0(\sup I-r_i)\) slope at the trial. The other direction
is identical. This proves (5), including endpoint clipping.
It uses the whole-box slope, not merely its midpoint value.

For fixed carrier and unweighted endpoints, let \(\mathcal E(\lambda)\)
be the maximum of (3) over the weighted coordinates, where
\(\lambda\) denotes the three reference parameters. Its derivative
is the reference derivative of \(D\) at the true maximizers;
there is **no optimizer derivative**. To see this without an
interior-optimizer assumption, sandwich the increment of the
maximum between the increments evaluated at the old and new
maximizers. Compactness and uniqueness make those maximizers
continuous. Dividing by the parameter increment gives the same
reference derivative from both sides, even at a clipped endpoint.

Let \(\mathcal H=\phi''\), \(d=X-U\), and put
\[
 P^{\rm row}=
  (2\pi iv-\tfrac\eta2g'(X_1+iH_1),
                  -2\pi iw-\tfrac\epsilon2g'(X_2+iH_2)).
 \tag{6}
\]
The exact reference gradients are
\[
 D_U=-\Re(\mathcal H d)-2\kappa_0d,\qquad
 D_H=\Im(P-P^{\rm row}+\mathcal H d).
 \tag{7}
\]
The Hessian is the original complex Schur complement of the
conditional index Hessian. Contract (7) with the validated original
two-leg response and the exact parameter derivatives, allowing each
weighted target to range through (5). This encloses the derivative
of \(\mathcal E\) on the whole parameter box. It neither
replaces a leg independently nor differentiates a numerical optimizer.

At the parameter midpoint \(\lambda_0\), enclose the target
slopes \(b(r_i;Z_0)\) separately. The exact one-sided concave
quadratic maxima from the
[previous pilot specification](research_mixed_attached_last_row_face_pilot.md)
give gains \(G_i^0\) such that
\[
 \mathcal E(\lambda_0)
        \le D(Z_0,r)+\sum_{i:\tau_i=1}G_i^0.
 \tag{8}
\]
In particular these gains use midpoint data only. If \(L_j\)
bounds the absolute envelope derivative from (7) and \(h_j\)
is the exact parameter half-width, then
\[
 \sup_{\lambda\ \mathrm{in\ box}}\mathcal E(\lambda)
 \le D(Z_0,r)+\sum_{i:\tau_i=1}G_i^0+\sum_{j=1}^3L_jh_j.
 \tag{9}
\]
The two parts are used together: midpoint-only target gains require
envelope derivatives evaluated on whole-box optimizer enclosures.
Using derivatives only at a fixed trial while also removing the
whole-box target gain would not prove (9).

All original phase values use the same primitive and lift. All
whole-box source/root/response acceptance remains outward; floating
operations can propose rational trials or root witnesses only.

## 4. One proposed low-height pilot, before any implementation

The proposed case is own type three, external types \((3,4)\),
boundary generator \(S_3\) in slot zero. Restrict the other
input to the bottom cap of \(K_4\), with heights between
\(-.108\) and \(-.102\). This is a subset of one of the
28 cases, not a proposed complete case sweep.

Let \(c_-=49/125-9i/125\), \(c_+=x_*+ih_*\), and set
\[
 \begin{split}
 c(t)&=(1-t)c_-+tc_+,\qquad h(u)=-\frac{27}{250}+\frac3{500}u,\\
 r(h)&=\sqrt{(3/50)^2-(h+13/250)^2},\\
 a(u,v)&=\frac3{10}+(2v-1)r(h(u))+ih(u),
              \qquad(t,u,v)\in[0,1]^3.
 \end{split}
 \tag{10}
\]
The radicand is at least \(29/62500>0\). This chart covers
the entire bottom cap, including both circle sides and both
horizontal ends, without a polar region at unrelated heights.
Its exact derivatives are
\[
 c_t=c_+-c_-,\qquad
 a_u=\frac3{500}\left(i-\frac{(2v-1)(h+13/250)}{r(h)}\right),
 \qquad a_v=2r(h).
 \tag{11}
\]
Thus no new clipping decision is needed to establish membership
of the parameters in this pilot chart. Interval hulls still only
accept through the original whole-box root test.

Proposed limits are 511 visited boxes and 30 seconds. A cyclic
split order would visit the lower child first for \(t,u\), and
the upper child first for \(v\), concentrating on low heights
and the right part of the type-four disk. Exact pending-volume
accounting and the previous deadline protection would be retained.
Both orientations, all carriers and the entire target square remain
mandatory. No previous fixed point is repeated: this slanted chord
starts at \(\Re c=.392\), while the earlier joint-corner check
had \(\Re c=.391\).

The slanted chord itself lies outside \(O_3\cup A_3\): its
height is below \(-.065\), while its real part exceeds \(.391\).
Consequently a positive pilot value there would refute only the
chosen sufficient \(K_3\) boundary comparison, not actual
open-word geometry. A negative partial run would prove no uniform
sign. The separate bounded driver implements only this subset.
The full 28-case family and all actual-word last-row signs remain
unproved by this design.
