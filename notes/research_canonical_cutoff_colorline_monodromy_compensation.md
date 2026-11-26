# Canonical cutoff continuation and compulsory color-line compensation

Private written proof, 18 November 2026.

The initial canonical cutoff can be continued from meridian one to
both endpoint sheets at an actual Alexander node. The entire original
finite-color polynomial then forces an exact compensating jump in its
endpoint amplitude. At the node this jump has an explicit exponential
size as the integer color grows. This proves neither failure nor success
of a particular physical continuation path; it rules out a uniformly
small error on both canonical branch paths.

## 1. The original germ and the node

Use the same canonical coefficients as [G] and [B]:
\[
 \widehat{\mathscr W}(h,Y)=\sum_{j\ge0}h^jW_j(Y),\qquad
 \mathcal B(Y,\xi)=\sum_{j\ge0}W_j(Y)\frac{\xi^j}{j!},
 \qquad h=\log Q.
 \tag{1}
\]
They are the original reduced, zero-framed one-component source.
The coefficients \(W_j\) are rational in \(Y\), with poles only at
zero and the Alexander divisor, and [G] proves their Gevrey-one
bound on every compact set avoiding those poles.

Let \(\alpha\ne0,1\) be a simple Alexander root satisfying the actual
operator-node hypotheses of [C]. Retain
\[
 z=Y-\alpha,\qquad r=\Delta_K'(\alpha)^{-1},\qquad
 \eta_*=\frac{B}{2A}\ne0,\qquad \beta^2=-\eta_*.
 \tag{2}
\]
Choose a logarithm \(a\) of \(\alpha\); necessarily \(a\ne0\).
It is retained throughout all color-line continuations below.

For a small nonzero cutoff \(R\), the local resolution in [C] is
\[
 \mathcal B(\alpha+z,\xi)
   =\frac1w H\left(z,w,\frac{z^3}{w^2}\right),\qquad
 w^2=z^2-\xi/\eta_*,\qquad H(0,0,0)=r.
 \tag{3}
\]
The function \(H\) is holomorphic on a fixed polydisk. Its domain
contains a \(w\)-annulus with inner radius a fixed multiple of
\(|z|^{3/2}\) and fixed small outer radius. Initially \(w=z\) at
\(\xi=0\). The two local endpoint sheets at \(\xi=R\) give the
canonical cutoffs \(U_{R,+}(h,z)\) and \(U_{R,-}(h,z)\) of [C].
They extend holomorphically through \(z=0\) for \(h\ne0\).

We choose the endpoint direction
\[
                   R=\varrho\,a/|a|,\qquad \varrho>0,
 \tag{4}
\]
with \(\varrho\) sufficiently small after the paths below have
been chosen. Other directions can be used for the continuation
statement; (4) makes its later quantitative consequence explicit.

## 2. Both node sheets come from the initial cutoff

First choose a fixed small nonzero \(z_0\) in the node chart.
Choose a compact path in the logarithmic meridian plane from
zero to a lift of \(\alpha+z_0\), whose final local logarithm is
\(a+\log(1+z_0/\alpha)\). Apart from the initial point, take the
path to avoid \(u=0\), and take its exponential image to avoid
the Alexander roots. Such a path exists because the forbidden
points form a discrete set in the logarithmic plane.
Its exponential image, with a small compact neighborhood, avoids
zero and the Alexander divisor.

The compact estimate [G] gives constants \(C,D\) there with
\(|W_j|\le CD^j j!\). Hence the actual series (1) converges normally
on that neighborhood and a common disk \(|\xi|<D^{-1}\).
The rational coefficients identify the germs on overlaps.
Choose \(R\) smaller than this common radius and sufficiently small
compared with \(z_0^2\). The straight-\(\xi\) cutoff
\[
       U_R(h,Y)=\frac1h\int_0^R e^{-\xi/h}\mathcal B(Y,\xi)\,d\xi
 \tag{5}
\]
therefore continues along the whole first path, jointly for
\(h\ne0\). At \(Y=\alpha+z_0\) it is the local source (3), with
the endpoint root \(w_R\) close to \(z_0\).
This identification uses the canonical coefficients, not a choice
of a new local solution.

We describe the remaining local continuation explicitly. Put
\[
                         \zeta^2=R/\eta_*.
 \tag{6}
\]
One can first rotate \(z_0\) at its fixed small modulus to the
direction of \(\zeta\), then move radially to \(3\zeta\).
For sufficiently small \(R\), these portions have
\(|w_R|\asymp|z|\), so \(|z^3/w_R^2|=O(|z|)\).
Next use \(z=\zeta t\), with a fixed bounded path from \(t=3\)
to \(t=0\) avoiding \(t=\pm1\). Along its finite portions away
from zero,
\[
 |w_R|^2=|\zeta|^2|t^2-1|,\qquad
 \left|\frac{z^3}{w_R^2}\right|
             =|\zeta|\frac{|t|^3}{|t^2-1|}=O(|\zeta|).
 \tag{7}
\]
The endpoint at \(z=0\) is handled by the holomorphic extension
in [C]. Thus this path reaches one of the two node sheets.

To reach the other, insert a local loop around \(z=\zeta\), for
example a circle
\[
                     z(t)=\zeta+\frac{\zeta}{4}e^{it},
                     \qquad 0\le t\le2\pi,
 \tag{8}
\]
joined to the preceding path by arcs avoiding \(z=\pm\zeta\).
On this circle \(|z|\asymp|w_R|\asymp|\zeta|\), and the last
quantity in (7) remains \(O(|\zeta|)\). Thus the entire loop is
inside the proved resolution for small \(R\). The function
\[
                         w_R^2=(z-\zeta)(z+\zeta)
 \tag{9}
\]
winds once around zero, so its continued square root changes sign.
The initial root \(w=z\) returns to itself.
This loop stays away from the unresolved inner region in (3);
no assertion about the individual singularities inside that region
is needed.

There is no additional integral ambiguity in this endpoint switch.
Under \(\xi=\eta_*(z^2-w^2)\), the cutoff differential becomes
\[
 -\frac{2\eta_*}{h}e^{-\eta_*z^2/h}
       e^{\eta_*w^2/h}H(z,w,z^3/w^2)\,dw.
 \tag{10}
\]
As proved directly in [C], its negative Laurent powers in \(w\)
are even, and the exponential preserves their parity. Its
\(w^{-1}\) coefficient is zero. Normal convergence on closed
subannuli therefore makes its integral independent of additional
winding in the allowed \(w\)-annulus.
The endpoint primitive and its holomorphic node extension in [C]
then identify the two continuations with exactly
\(U_{R,+}\) and \(U_{R,-}\), with the endpoint labels fixed there.

The local loops lie in a disk about \(\alpha\) not meeting zero.
Their logarithms therefore return to the same value \(a\) at
the node. We have proved that both canonical node sheets are
continuations of the same initial cutoff (5), along two specified
logarithmic meridian paths. The paths can be fixed independently
of the positive integer color.

## 3. The entire scalar terms and exact compensation

Fix an integer color \(L\ge1\). On the color line
\[
                          Y=e^u,\qquad h=u/L,
 \tag{11}
\]
the original finite polynomial \(C_L(e^{h/2})\) is entire in \(h\),
and hence in \(u\). Write
\[
 C_L(e^{h/2})=\sum_{j\ge0}c_{L,j}h^j,\qquad
 A_L(h,R)=\sum_{k,m\ge0}c_{L,k+m}h^k\frac{R^m}{m!}.
 \tag{12}
\]
The latter scalar endpoint amplitude is also entire in \(h\)
for each fixed \(L,R\). To see this without a uniform-color
assumption, express the finite Laurent polynomial as a finite sum
\(\sum_\nu a_\nu e^{\gamma_\nu h}\). Its contribution to the
double series has absolute value bounded on compact sets by
\[
 |a_\nu|\sum_{k,m\ge0}
 \frac{|\gamma_\nu h|^k|\gamma_\nu R|^m}{(k+m)!\,m!}
 \le |a_\nu|e^{|\gamma_\nu h|+|\gamma_\nu R|}.
 \tag{13}
\]
The finite sum proves normal convergence. No uniformity in \(L\)
is asserted in (13).

The exact initial identity from [B] is
\[
 U_R(h,e^{Lh})=C_L(e^{h/2})
                      +e^{-R/h}\mathcal H_L(h),\qquad
 \mathcal H_L=K_L-A_L.
 \tag{14}
\]
Here \(K_L\) is the actual semigroup endpoint term, not a free
homogeneous correction. Initially \(\mathcal H_L\) is holomorphic
at \(h=0\).

Follow either logarithmic path of Section 2, starting at a small
nonzero \(u\), and substitute \(h=u/L\). The paths avoid \(u=0\).
The cutoff is jointly holomorphic for \(h\ne0\), so it has the
continuations already constructed. The scalar polynomial and
\(A_L\) have no branch ambiguity. Consequently (14) continues
exactly, and specifies the corresponding continuation of \(K_L\)
and \(\mathcal H_L\). This is analytic continuation of the actual
initial identity; it does not add a newly chosen correction.

At the common endpoint \(u=a\), put \(h_L=a/L\). Subtracting the
two continued identities gives
\[
 \begin{split}
 \mathcal H_{L,+}(h_L)-\mathcal H_{L,-}(h_L)
 &=K_{L,+}(h_L)-K_{L,-}(h_L)\\
 &=e^{LR/a}\{U_{R,+}(h_L,0)-U_{R,-}(h_L,0)\}.
 \end{split}
 \tag{15}
\]
The displacement argument of the local cutoffs on the right is
zero. Both the original color and the same logarithm \(a\) have
been retained.

## 4. The compulsory compensation has an explicit size

By (4), the sequence \(h_L=a/L\) lies in a closed sector facing
the fixed endpoint \(R\). The exact node profile of [C], at its
scaled coordinate \(s=0\), gives
\[
 U_{R,+}(h_L,0)-U_{R,-}(h_L,0)
       =C_* (L/a)^{1/2}(1+o(1)),\qquad
 C_*=2\beta r\sqrt\pi\ne0.
 \tag{16}
\]
The square root and endpoint orientation are precisely those of
[C]; its nonzero modulus does not depend on relabeling the two
sheets. Thus (15) proves the actual integer-color asymptotic
\[
 \mathcal H_{L,+}(h_L)-\mathcal H_{L,-}(h_L)
       =C_* (L/a)^{1/2}e^{LR/a}(1+o(1)).
 \tag{17}
\]
In particular its modulus is asymptotic to
\[
                 |C_*|\sqrt{L/|a|}
                         \exp(\varrho L/|a|).
 \tag{18}
\]
Integer-color single-valuedness forces this compensation; it
does not exclude it.

There is a corresponding statement directly about the actual
cutoff errors. Let
\[
 E_{L,\pm}=U_{R,\pm}(a/L,0)-C_L(e^{a/(2L)}).
 \tag{19}
\]
For all sufficiently large integers \(L\),
\[
       \max(|E_{L,+}|,|E_{L,-}|)
          \ge\frac12|E_{L,+}-E_{L,-}|
          \ge c\sqrt L .
 \tag{20}
\]
This does not assert that the same branch realizes the maximum
for every \(L\). It also does not rule out exponentially accurate
matching along one suitably selected path. It does show that a
bound keeping both continued errors exponentially small at the
node is incompatible with the exact original source.

## 5. Paid connection and remaining selection

The global compact Borel germ pays continuation of the initial
cutoff to the local node chart. The resolved endpoint geometry pays
both canonical branch paths without a full moving-singularity
theorem. Entire finite-color scalar terms then give the exact
compensation law and its quantitative lower bound.

What remains is a quantitative statement for one source-selected
path, retaining its continued \(K_L\) and the original observation.
Neither monodromy integrality nor integer-color single-valuedness
removes that term: equations (15)--(18) compute its compulsory
branch difference. The result does not identify the operator
component with the hyperbolic representation component, continue
to the physical complete-root point, or prove a scalar volume lower
bound. Its simple-node hypotheses are not asserted for every
arbitrary short partial filling, including those with no Alexander
pole seed.

## 6. Complete proof sources

| Label | Complete source | SHA256 |
|---|---|---|
| G | notes/research_classical_verma_borel_pole_profile.md | 6ba957d7a521524f370cb3bdd90ab30338bff8c13960ae6ca1825d08260c77d2 |
| C | notes/research_canonical_cutoff_node_regularization_and_profile.md | 8c28a3d3a7b11085c8e2b5966221501b632ea99600aae4db57e8bdf8cd4a9631 |
| B | notes/research_canonical_borel_finite_laplace_current.md | b3b1e4246e2b5ed1b364585b8504edf8e0f1f1e15797f62f276fc4b89dca586f |

G supplies the actual rational coefficients and compact Gevrey bound.
C supplies the convergent resolved source, zero-residue primitive,
canonical endpoint sheets and node profile. B supplies the original
exact color-line endpoint identity. The continuation paths,
entire scalar amplitude, compulsory compensation and its size are
proved above. No external proof, mathematical program, test or build
is used. Frozen notes and public manuscripts are unchanged.
