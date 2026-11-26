# The exact moving branch locus of the canonical node source

Private written proof, 18 November 2026.

The canonical source in [L] is known outside a narrow Borel cluster.
Here the actual noncharacteristic extension theorem [E] and an explicit
family of smooth barriers continue that same source throughout a
punctured neighborhood of the exact classical action graph. No
regularity or smoothness of the unknown singular support is assumed.

The result locates the local branch locus and retains its nonzero
two-sheet monodromy. It does not prove that the source is a regular
square-root pole on that locus: an essential singularity on the
square-root cover is not excluded. Nor does it identify the partner
branch as geometric, continue it to a complete meridian, or give a
lower bound for the original closed invariant.

The nonremovable source branch also forces every other analytic
actual annihilator to contain the same local classical branch. This
is a source consequence, not an assumed equality of operator ideals.

## 1. Actual operator, action, and assertion

Use the canonical Borel source and the actual operator node of [L].
Thus \(\alpha\ne0,1\) is a simple Alexander root, and the displayed
actual finite-shift annihilator has coefficients holomorphic near
\((h,Y)=(0,\alpha)\). Its classical symbol satisfies
\[
 P(Y,1)\equiv0,\qquad P_L(\alpha,1)=0,\qquad
 P_{LL}(\alpha,1)P_{YL}(\alpha,1)\ne0.
 \tag{1}
\]
All state gauges are those of [L]. In particular (1) is not imposed
on a classically extracted factor which has not been shown to be an
actual annihilator.

Choose the logarithmic meridian centered at the node,
\[
 u=\log(Y/\alpha),\qquad z(u)=\alpha(e^u-1),\qquad
 \mathcal P=\sum_i p_i(h,u)T^i,\quad Tf(u)=f(u+h).
 \tag{2}
\]
The harmless translation of the logarithm does not change the
finite-shift convention of [E]. Write \(P(u,L)\) for the symbol in
this coordinate. An elementary holomorphic factorization gives
\[
       P(u,L)=(L-1)(L-\ell(u))Q(u,L),\qquad
 \ell(0)=1,\quad \ell'(0)\ne0,\quad Q(0,1)\ne0.
 \tag{3}
\]
Indeed divide the symbol by \(L-1\); its derivative in \(L\) at
the node is \(P_{LL}/2\ne0\), so the implicit function theorem
gives \(\ell\), and holomorphic division gives \(Q\).
This is only a factorization of the symbol. The full actual
operator is used in every application of [E].

Let \(\log\ell(0)=0\), and define the analytic action
\[
                 S(0)=0,\qquad S'(u)=\log\ell(u).
 \tag{4}
\]
In the notation of [L],
\[
 \eta_*=\frac{B}{2A}\ne0,\qquad
                 S(u)=-\eta_*z(u)^2+O(u^3).
 \tag{5}
\]
This is the complete analytic action (4), not a quadratic or
cubic truncation. Introduce
\[
                         \rho=\xi+S(u).
 \tag{6}
\]

**Theorem.** There are \(b_*,R_*>0\) such that the canonical Borel
source, on its specified initial sheets, continues holomorphically
to the actual twofold cover
\[
       |u|<b_*,\qquad 0<|\rho|<R_*,
                       \qquad \tau^2=\rho .
 \tag{7}
\]
For every sufficiently small \(u\), its monodromy under
\(\tau\mapsto-\tau\) is nontrivial. Thus the only inner locus that
must be removed is exactly
\[
                              \xi=-S(u).
 \tag{8}
\]
In particular there is no additional inner singular point or
curve away from (8) on this continued cover.

The theorem asserts holomorphy for \(\tau\ne0\) and nonremovability
on the base. It asserts neither a finite Laurent principal part
at \(\tau=0\) nor a convergent fractional-power amplitude there.
All continued primitive and semigroup histories are retained when
using [E]; they are not set to zero in choosing this continuation.

## 2. The constructed outer domain and its cover

The exact resolution in [L] is
\[
 b(u,\xi)=\frac1w H\!\left(z(u),w,\frac{z(u)^3}{w^2}\right),
 \quad w^2=z(u)^2-\frac{\xi}{\eta_*},\quad H(0,0,0)=r\ne0.
 \tag{9}
\]
Here \(H\) is holomorphic on a fixed polydisk, and this expression
is the actual canonical continuation, not a separately chosen
solution. Put
\[
          g(u)=z(u)^2+\frac{S(u)}{\eta_*}=O(u^3).
 \tag{10}
\]
Then \(w^2=g(u)-\rho/\eta_*\). Consequently there are constants
\(C_H,b_0,R_0>0\) for which (9) is jointly holomorphic whenever
\[
            |u|<b_0,\qquad C_H|u|^3<|\rho|<R_0
 \tag{11}
\]
on its twofold cover. To verify this directly, take \(C_H\)
large enough that \(|\eta_*g(u)/\rho|<1/2\) and
\(|z(u)^3/w^2|\) stays strictly inside the third disk for \(H\).
Then shrink \(b_0,R_0\) so that \(z,w\) stay inside its other
two disks.

On (11), choose a constant \(\beta\) with \(\beta^2=-1/\eta_*\).
There is the explicit cover identification
\[
 w=\beta\tau
       \left(1-\frac{\eta_*g(u)}{\rho}\right)^{1/2},
 \qquad \tau^2=\rho,
 \tag{12}
\]
where the second square root is its convergent branch near one.
It is an analytic unit. Thus the initial cover is exactly the
\(\sqrt\rho\) cover; there is no extra \(u\)-monodromy.

The required source histories are available on this initial
continuation. One may retain their path labels throughout. The
Laurent description in [L] also checks why no primitive has been
silently simplified: for fixed \(u\), the negative \(w\)-powers
of \(b\) are odd, while its even powers are nonnegative.
The differential \(d\xi=-2\eta_*w\,dw\) therefore has no residue
term when multiplied by \(b\). Derivatives at fixed \(\xi\) and
successive \(\xi\)-primitives preserve this parity property.
Their convergent sums on compact annuli give the same continued
histories as their canonical initial germs. No logarithmic
integration constant is discarded.

Fix a constant \(C>C_H\), with a strict margin, and shrink
\(b_0,R_0\) further below. In particular the surfaces
\(|\rho|=C|u|^3\), away from \(u=0\), and their compact collars
are inside the already known open set (11).

## 3. Noncharacteristic radial barriers

Since \(S''(0)=\ell'(0)\ne0\), choose \(\kappa,K>0\) and
\(b_0>0\) so that
\[
          \kappa |u|\le |S'(u)|\le K|u|,
                         \qquad 0<|u|\le b_0.
 \tag{13}
\]
Also shrink the neighborhood so that \(Q(u,e^p)\ne0\) for
the small \(u,p\) used below. All nonzero logarithmic aliases
of the two roots in (3) lie outside this small \(p\)-neighborhood.

Let \(t=|u|\), and let \(r(t)>0\) be \(C^2\) on a compact
annulus \(a\le t\le b\), where \(0<a<b\le b_0\). Consider the
inner boundary
\[
                 |\rho|=r(t),\qquad \rho=\xi+S(u),
 \tag{14}
\]
with known side \(|\rho|>r(t)\).
For the defining function \(|\rho|^2-r(t)^2\), its complex
normal has nonzero \(\xi\)-component. Its ratio in the original
\((u,\xi)\) coordinates is exactly
\[
 p_{\rm nor}
 =S'(u)-\rho\frac{r'(t)}{r(t)}\frac{\bar u}{t}.
 \tag{15}
\]
Indeed the two Wirtinger derivatives are
\(\bar\rho S'-rr'\bar u/t\) and \(\bar\rho\).

Assume
\[
                         0<r'(t)<\frac{\kappa t}{2}.
 \tag{16}
\]
On (14) the distance of (15) from the partner slope \(S'(u)\)
is precisely \(r'(t)>0\), whereas
\[
              |p_{\rm nor}|
                    \ge |S'(u)|-r'(t)>\frac{\kappa t}{2}.
 \tag{17}
\]
Its magnitude is at most \((K+\kappa/2)t\). For small \(b_0\),
(3), (13), and the exclusion of logarithmic aliases give
\[
                         P(u,e^{p_{\rm nor}})\ne0.
 \tag{18}
\]
This tests the full displayed actual symbol, including \(Q\).
It does not divide a quantum operator by either root factor.

Every point of (14) is therefore an actual noncharacteristic
boundary point in the sense of [E, Section 7]. That theorem
extends the source and its continued companions from the known
side, without a bound on their norms near the boundary. The
surface (14) is our chosen auxiliary barrier. No smoothness of
the unknown singular support has been used.

## 4. A nested barrier reaching any punctured target

We give the profile construction explicitly. It is the reason
there is no repeated loss of meridian radius at every Borel step.

Choose \(b>0\) sufficiently small once and for all, with
\(Cb^3<R_0/2\). Let a target satisfy
\[
                  0<t_0=|u_0|<b/4,\qquad
                          0<|\rho_0|<R_0/2.
 \tag{19}
\]
Targets already in (11) need no extension. For the others,
choose \(a<t_0/4\) and a positive \(\varepsilon<1\) so small that
\[
             3a+\varepsilon b
                        <\left(\frac{|\rho_0|}{2C}\right)^{1/3}.
 \tag{20}
\]

Construct a smooth increasing function \(\phi_{\rm flat}\)
which equals \(t\) for \(t\le2a\), decreases its derivative
smoothly from \(1\) to \(\varepsilon\) on \([2a,3a]\), and has
derivative \(\varepsilon\) afterward. Thus
\[
 0<\phi_{\rm flat}\le t,\quad
 0<\phi_{\rm flat}'\le1,\quad
       \phi_{\rm flat}(t)\le3a+\varepsilon b
                      \quad(3a\le t\le b).
 \tag{21}
\]
Take a smooth decreasing cutoff \(\chi\), equal to one through
\(b/2\) and zero from \(3b/4\) onward, with
\(|\chi'|\le K_0/b\) for an absolute constant \(K_0\).
Put
\[
 \phi(t)=t-(t-\phi_{\rm flat}(t))\chi(t),\qquad
 r_0(t)=Ct^3,\qquad r_1(t)=C\phi(t)^3.
 \tag{22}
\]
Then \(0<\phi\le t\), \(\phi'>0\), and
\(\phi'\le K_1:=2+K_0\). The last bound follows directly from
differentiating (22), using \(\chi'\le0\).
The profiles agree near both annulus ends, and
\[
 r_1\le r_0,\qquad r_1(t_0)<|\rho_0|/2,\qquad
             0<r_j'(t)\le3CK_1t^2\quad(j=0,1).
 \tag{23}
\]
Choose \(b\) small enough that \(3CK_1b<\kappa/2\). Both
profiles obey (16), as does their convex homotopy
\[
                    r_\lambda=(1-\lambda)r_0+\lambda r_1,
                          \qquad 0\le\lambda\le1.
 \tag{24}
\]
The derivatives remain strictly positive on the fixed compact
annulus. They can be very small; no uniform lower bound over
all possible targets is claimed or needed.

Define nested domains, on the \(\sqrt\rho\) cover, by
\[
 \Omega_\lambda=
   \{\,a<|u|<b,\quad r_\lambda(|u|)<|\rho|<R_0/2\,\}.
 \tag{25}
\]
The source is already known on a neighborhood of the initial
domain's boundary collars. Near both \(u\)-annulus ends the
profile does not change; the outer \(\rho\)-boundary also remains
in the known region. The only moving boundary is the compact
inner surface (14), and (18) holds throughout its homotopy.

## 5. Continuation through the entire barrier homotopy

Here is the compactness argument, including its source and sheet
conditions. Start with the actual germ on \(\Omega_0\). Continue
it and the retained primitive and bounded-\(s\) semigroup histories
locally using [E] as the inner boundary moves inward.

Suppose the construction had a first stopping parameter
\(\lambda_*\le1\). The compatible earlier continuations define
the source on the full known side of the boundary of
\(\Omega_{\lambda_*}\): their union is that domain, with the
fixed collars supplied by the initial continuation. At every
point on its moving inner boundary there is therefore a
one-sided joint source and its continued companions. Any
interior base point has a finite continuation chain from the
initial germ. This is the history data required by [E]; a
uniform bound on those histories is not assumed.

The boundary is \(C^2\), its \(\xi\)-normal is nonzero, and
(18) holds. The shrinking-slab argument of [E, Section 7]
therefore extends the actual source and its companions across
each such point. Its coefficient neighborhood is fixed locally;
the source slab has meridian radius proportional to
\(\sqrt\epsilon\) and primitive length \(O(\epsilon)\).
Consequently the convergence threshold is
\(O(\epsilon/\sqrt\epsilon)\), independent of the possibly
large finite history norms. This is an extension across the
given boundary, not an estimate that consumes a preassigned
global meridian buffer at each step.

The moving boundary is compact. Choose a finite family of these
extension patches, refined small enough that their overlaps
meeting the boundary also meet the connected known side.
The extensions agree there by analytic uniqueness and hence
glue. Together with the fixed end collars and outer collar,
they give a neighborhood of the closure of the relevant
domain. Continuity of (24) then includes
\(\Omega_{\lambda_*+\delta}\) for some \(\delta>0\), unless
\(\lambda_*=1\), in which case it includes the final boundary.
This contradicts a first stopping parameter. Equivalently,
the usual supremum of parameters reached by compatible local
continuations cannot be less than one. The construction
therefore reaches \(\Omega_1\), which contains the target (19).

The argument can be performed with all history paths labelled,
on a finer continuation cover if necessary. The function \(b\)
itself glues on the original twofold cover. Indeed inclusion
\(\Omega_0\subset\Omega_\lambda\) is a radial deformation
equivalence: only the lower radius in each \(\rho\)-annulus has
changed. It introduces no new loop generator. Local
extensions agreeing on the known side preserve the initial
deck relations. Thus a possible extra path label on a
primitive is not imposed as an extra sheet of \(b\).

Different choices of target and profiles are compatible. Their
radial domains intersect in connected radial domains containing
the same outer collar, on each continued cover. The functions
there agree by the identity theorem. Taking their union gives
\[
                 0<|u|<b/4,\qquad 0<|\rho|<R_0/2
 \tag{26}
\]
on the actual twofold cover. This construction does not
approach \(\rho=0\) by infinitely many steps at one fixed
meridian radius. For each nonzero target it uses one compact
annulus, a finite barrier homotopy, and anchored end collars.

At \(u=0,\rho\ne0\), (9) is already jointly holomorphic after a
local square-root choice. The new continuation agrees with
that germ on the old outer domain. Analytic uniqueness glues
these neighborhoods across \(u=0\), proving the holomorphy
assertion (7), after decreasing \(b_*,R_*\) if needed.

## 6. Nonremovability and precise singularity scope

Choose one fixed small \(\rho_b\ne0\) in the outer known region.
By (9), (12), and \(H(0,0,0)=r\ne0\), shrink \(\rho_b\) and
then the \(u\)-disk so that both values of \(H\) at the two
lifts remain within \(|r|/4\) of \(r\). At that base point,
\[
 b_+(u,\rho_b)-b_-(u,\rho_b)
  =\frac{
       H(z,w,z^3/w^2)+H(z,-w,z^3/w^2)}{w}
                         \ne0.                    \tag{27}
\]
The identification of the two sheets is the original one,
not a new relative sign choice. This nontrivial monodromy
persists through all the compatible continuations in Section 5.

For any fixed sufficiently small \(u\), if the branch at
\(\rho=0\) were removable as a single-valued holomorphic
function of \(\rho\), its monodromy on a punctured neighborhood
would be trivial. Uniqueness would then make (27) zero on the
outer base, a contradiction. Thus (8) is a genuine branch
locus for each such \(u\), while (7) excludes any other inner
singularity on the continued cover.

This conclusion must be distinguished from a local form such as
\(\rho^{-1/2}A(u,\rho)+B(u,\rho)\) with \(A,B\) holomorphic at
\(\rho=0\). We have not proved that form, a finite pole order
on the \(\tau\)-cover, or a uniform growth estimate as
\(\tau\to0\). The theorem locates the exact moving branch
locus and its nonzero two-sheet monodromy only.

## 7. The branch is intrinsic to the actual source

Let another finite-shift operator
\[
 \mathcal Q=\sum_j q_j(h,u)T^j,\qquad
 Q_{\rm cl}(u,L)=\sum_jq_j(0,u)L^j
 \tag{28}
\]
annihilate the same actual canonical formal source, with coefficients
holomorphic on the node neighborhood. Its original state gauge is
retained. The source equation and its primitive histories are those
of [E], now with these coefficients. A classical symbol which is
identically zero gives a vacuous assertion; otherwise
\[
                         Q_{\rm cl}(u,\ell(u))=0.
 \tag{29}
\]

Indeed fix any sufficiently small \(u_1\ne0\), and suppose that the
left side of (29) were nonzero there. On a meridian disk about
\(u_1\), choose one branch of the continued source on the half-disk
\(\operatorname{Re}\rho>0\), with \(\rho=\xi+S(u)\).
Section 5 supplies its joint continuation and retained companions.
For the operator (28), the complex normal ratio at
\(\rho=0,u=u_1\) is \(S'(u_1)\), and
\[
 Q_{\rm cl}(u_1,e^{S'(u_1)})
                    =Q_{\rm cl}(u_1,\ell(u_1))\ne0.
 \tag{30}
\]
The actual extension theorem [E] would extend that half-disk branch
holomorphically through \(\rho=0\). Its analytic continuation around
a sufficiently small circle would then be trivial. By uniqueness on
the punctured cover this contradicts (27). Hence (29) holds at every
such \(u_1\), and the identity theorem extends it across \(u=0\).
The proof works for each finite set of shifts: the companion
continuation retains \(c_s\) on every bounded \(s\)-set, and thus
supplies the histories required by any particular (28).

Holomorphic division in \(L\) now gives local branch divisibility
\[
                 Q_{\rm cl}(u,L)
                      =(L-\ell(u))Q_1(u,L)
 \tag{31}
\]
near \((0,1)\). This is classical local divisibility, not a
right-factor identity for the quantum operator.

If the selected branch lies on an irreducible algebraic curve
\(F(Y,L)=0\), then every rational classical symbol of an actual
annihilator has that algebraic factor after coefficient denominators
are cleared. For example this applies when the chosen actual symbol
in (1) has rational coefficients. To justify the assertion, an
analytic branch with varying \(Y\) is not vertical. If a polynomial
numerator vanished on it but were relatively prime to \(F\), their
resultant in \(L\), after removing irrelevant leading factors, would
give a nonzero polynomial in \(Y\) vanishing on an open set.
This is impossible. Thus \(F\) divides the numerator.
No algebraic factor statement is made for arbitrary analytic
coefficient functions beyond the local division (31).

The partner in this theorem therefore cannot be dismissed as a
classical factor introduced only by a chosen left multiple: its
nonzero canonical monodromy forces its occurrence for every
displayed analytic actual annihilator. This still does not identify
it with the hyperbolic representation component.

## 8. Complete proof sources and limits

| Label | Complete proof direct | SHA256 |
|---|---|---|
| E | notes/research_actual_borel_analytic_elliptic_inverse.md | d84ffc6794bd05917168595ec909fcb739e693b7c7574dea7471a404fa328e55 |
| L | notes/research_classical_verma_borel_laurent_resolution.md | 6a65d3f47544255c46e6cc5450d822b5b38cfccce591e5ad59e21d4c569be341 |

L supplies the actual canonical outer resolution, its original
sheets, the node hypotheses, and the action calibration (5).
E supplies the convergent actual-source extension through a
supplied \(C^2\) noncharacteristic boundary, with its histories.
The radial profiles, normal computation, compact homotopy,
cover control, and nonremovability are proved above.

No general propagation-of-singularities or resurgence theorem
has been imported. The exact action graph belongs to the
specified actual operator branch. Its membership in the
geometric representation component, global continuation to
the physical observation, a comparison of all remaining
contour contributions, and a lower bound for the original
complete-color invariant remain separate tasks. In particular
the broad arbitrary-short-filling target includes cores for
which this simple Alexander node is absent.

Only written mathematics and complete source-text reads were
used. No mathematical programs, tests, or builds were run.
Frozen notes and public manuscripts are unchanged.
