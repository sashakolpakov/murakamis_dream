# Exact local action support at a higher collision

Private written proof, 18 November 2026.

The joint continuation in [J] supplies actual annuli around every
exceptional partner singularity. An explicit noncharacteristic barrier
shrinks each such cluster to its exact classical action graph.
The argument uses the original finite-shift equation and retains its
primitive and semigroup histories.

All assertions are local to one partner cluster and to specified finite
angular windows on its continuation cover. No uniform meridian radius
over infinitely many windings, removal of the possible Borel origin
divisor on other sheets, or regular square-root minor is asserted.

## 1. Source, exact branches, and the local statement

Use the actual canonical source and finite-shift operator of [J],
including its simple Alexander root \(\alpha\ne0,1\).
Thus \(h=\log Q\), \(z=Y-\alpha=s^p\), \(p\ge1\), and
\[
 \mathcal P_h=\sum_i p_i(h,Y)T^i,\qquad Tf(Y)=f(e^hY).
 \tag{1}
\]
Its coefficients are holomorphic near \((0,\alpha)\), and its
classical symbol \(P(Y,L)\) satisfies [J, (3)]:
\[
 P(Y,1)\equiv0,\quad P_{YL}(\alpha,1)\ne0,\quad
 \partial_L^aP(\alpha,1)=0\ (2\le a\le p),\quad
 \partial_L^{p+1}P(\alpha,1)\ne0.
 \tag{2}
\]
The actual source forces \(P_L(\alpha,1)=0\).
Put \(\omega=p+1\) and
\[
 u(s)=\log\frac{\alpha+s^p}{\alpha},\qquad
 u'(s)=\frac{p s^{p-1}}{\alpha+s^p}.
 \tag{3}
\]
The actual difference step is translation by \(h\) in \(u\);
we do not replace it by a translation in \(s\).

Here is the elementary classical branch construction. Dividing only
the classical symbol by \(L-1\), and putting \(L=1+v\), gives
\[
 P(\alpha+s^p,1+v)
 =v\{q_Ys^p+q_Lv^p+O(s^{2p},s^pv,v^{p+1})\},
 \quad
 q_Y=P_{YL}(\alpha,1),\qquad
 q_L=\frac{\partial_L^{p+1}P(\alpha,1)}{(p+1)!}.
 \tag{4}
\]
After \(v=s\lambda\), division of the braces by \(s^p\) is
holomorphic and equals \(q_Y+q_L\lambda^p\) at \(s=0\).
Its \(p\) roots are distinct and nonzero. The analytic implicit
function theorem gives branches
\[
 \ell_j(s)=1+\lambda_js+O(s^2),\qquad
 \lambda_j^p=-q_Y/q_L,\qquad 1\le j\le p.
 \tag{5}
\]
Successive holomorphic division by these roots gives
\[
 P(\alpha+s^p,L)=(L-1)\prod_{j=1}^p(L-\ell_j(s))Q(s,L),
                         \qquad Q(0,1)\ne0 .
 \tag{6}
\]
Division is valid also at \(s=0\): after each division the next
root vanishes in the quotient for \(s\ne0\), and the identity
extends holomorphically. Negative powers of \(L\) are harmless
units near one. This is not a factorization of the quantum operator.

Let \(l_j(s)=\log\ell_j(s)\), with \(l_j(0)=0\), and define the
full analytic actions
\[
 S_j(0)=0,\qquad S_j'(s)=u'(s)l_j(s),\qquad
 \eta_j(s)=-\frac{S_j(s)}{s^\omega}.
 \tag{7}
\]
The last expression extends holomorphically across zero, with
\[
 \eta_j(0)=\eta_j^*=-\frac{p\lambda_j}{\alpha(p+1)}.
 \tag{8}
\]
These are exactly the distinct nonzero critical points of [J].
Indeed their \(p\)-th powers equal
\(p^p/((p+1)^p\kappa)\) in that note's normalization.
Fix one index \(j\), and set
\[
                       \rho=\xi+S_j(s).
 \tag{9}
\]

Use real angular labels \(\sigma=\arg s\), \(\theta=\arg\rho\)
on the universal cover where \(s\rho\ne0\).
A finite angular window means a bounded open rectangle in
\((\sigma,\theta)\), with a smaller closed rectangle in its interior.
It need not have width less than \(2\pi\).

**Local support theorem.** There is a sufficiently small fixed
\(\delta>0\), depending on the actual operator, with the following
property. Specify a finite angular window and an actual outer source
branch obtained by a finite path provided by [J], avoiding its zero
and exceptional critical points after leaving the canonical germ.
There is \(b>0\), possibly depending on that window and
path, such that this source and its retained companions continue
holomorphically to
\[
 0<|s|<b/4,\qquad 0<|\rho|<\delta|s|^\omega
 \tag{10}
\]
on the smaller angular rectangle.
Different target constructions agree wherever their prescribed outer
branches agree.

For the canonical pair obtained by circling the \(j\)-th exceptional
fold, monodromy about \(\rho=0\) is nontrivial for every sufficiently
small nonzero \(s\). Thus the exact local partner divisor is
\[
                            \xi=-S_j(s).
 \tag{11}
\]
There is no extra support in the punctured cluster (10) on these
continued charts.

The conclusion is a germwise statement on every prescribed finite
part of the continuation cover. A single \(b\) for all possible
windings or outer continuation words is not claimed. Nor is an
extension through \(s=0\) at fixed nonzero \(\xi\) claimed.

## 2. The actual outer annulus and its histories

Write the ramified source of [J] as
\[
 b_p(s,\eta)=s^p\widehat W(\alpha+s^p,s^\omega\eta),
 \tag{12}
\]
where \(\widehat W\) is the original \(h\)-Borel transform.
Theorem [J] continues \(b_p\) jointly near every finite path avoiding
zero and the exceptional critical points, with a positive \(s\)-radius
for that path.

Choose \(\delta\) so small that
\[
       \{\eta:\delta/2<|\eta-\eta_j^*|<3\delta\}
 \tag{13}
\]
is disjoint from zero and the other exceptional points. On every
finite angular portion of the universal cover of (13), [J] supplies
one common positive \(s\)-radius: use a finite collection of path
charts and the minimum of their radii. The same applies after a
specified finite initial continuation word.

Since \(\eta_j(s)=\eta_j^*+O(s)\), shrink that radius so that
\(|\eta_j(s)-\eta_j^*|<\delta/10\). Substitution
\[
                  \eta=\eta_j(s)+\rho/s^\omega
 \tag{14}
\]
then gives the actual source on a buffered outer annulus
\[
 \delta|s|^\omega<|\rho|<2\delta|s|^\omega
 \tag{15}
\]
over each specified finite angular window. Its source is
\(s^{-p}b_p(s,\eta)\), with the branch continued from (12).

Both angular labels matter in (14). As \(s\) winds with \(\rho\)
fixed, \(\rho/s^\omega\) winds in the opposite direction.
On a finite window its lifted angle has a finite range, so the
finite-chart construction just described applies. We make no
identification of sheets after a prescribed number of turns.

The hypotheses on companions in [E] are also paid on this initial
domain. At any point with \(s\ne0\), use the local inverse of (3).
The finite Borel paths used above and a smaller meridian neighborhood
give a compact joint continuation strip in the original \((u,\xi)\)
coordinates. One obtains it by shrinking the meridian disk through
the finitely many path charts. At fixed \(s\) the exact primitive
adapter, for \(a\ge1\), is
\[
 I_\xi^a\widehat W
        =s^{\omega a-p}I_\eta^a b_p
 \tag{16}
\]
with the same scaled path and its complete initial history.
The original \(I_\xi\partial_u\) semigroups can equivalently be
constructed on the joint strip. A meridian buffer \(d>0\) and path
length \(L_0\) bound their \(n\)-th term on bounded parameter sets by
\[
                      M\frac{(|t|L_0/d)^n}{n!}.
 \tag{17}
\]
Thus they and their primitive histories converge normally, and
agree with their original germs. All later extensions use [E]'s
companion extension as well as its extension of \(\widehat W\).
No primitive is restarted at a new origin.

## 3. Separation of all characteristic slopes

By (3), (5), and (6), after shrinking \(b\) there are constants
\(\gamma,\gamma_u,K>0\) such that, with \(t=|s|\),
\[
 \begin{split}
 &|l_j(s)|\ge\gamma t,\qquad
   |l_j(s)-l_k(s)|\ge\gamma t\quad(j\ne k),\\
 &|u'(s)|\ge\gamma_u t^{p-1},\qquad |l_j(s)|\le Kt .
 \end{split}
 \tag{18}
\]
In a fixed small logarithmic slope neighborhood, the only roots
of \(P(\alpha+s^p,e^\zeta)\) are \(0,l_1(s),\ldots,l_p(s)\).
The residual factor in (6) is a unit there and all nonzero
\(2\pi i\)-aliases are outside it.

Let \(r=r(t,\sigma,\theta)>0\) be a real \(C^2\) radial profile on
a compact radial and angular box. On the boundary
\[
                            |\rho|=r(t,\sigma,\theta)
 \tag{19}
\]
the known side will be \(|\rho|>r\).
For its defining function
\(\mathfrak f=|\rho|^2-r^2\), the exact complex normal ratio in
the original logarithmic meridian coordinate is
\[
 \boxed{\quad
 \zeta_{\rm nor}
  =l_j(s)-
   \frac{\rho\,\bar s/t}
        {r\,u'(s)(1+i r_\theta/r)}
                         (r_t-i r_\sigma/t).
 \quad}
 \tag{20}
\]
For verification,
\[
 \mathfrak f_\xi=\bar\rho(1+i r_\theta/r),\qquad
 \mathfrak f_s=\mathfrak f_\xi S_j'(s)
                         -r(\bar s/t)(r_t-i r_\sigma/t),
 \tag{21}
\]
and \(\mathfrak f_s=u'(s)\mathfrak f_u\).
These are Wirtinger derivatives; all derivatives of \(r\) in
(20)--(21) are real derivatives. In particular
\(\mathfrak f_\xi\ne0\).

If
\[
       r_t>0,\qquad
       |r_t|+|r_\sigma|/t\le K_1\delta t^p,
 \tag{22}
\]
then the correction in (20) is nonzero and has modulus at most
\[
                         (K_1/\gamma_u)\delta t.
 \tag{23}
\]
Indeed \(1+i r_\theta/r\ne0\) has modulus at least one,
and \(r_t-i r_\sigma/t\ne0\) because \(r_t>0\).
Choose \(\delta\) small enough that the upper bound is less than
\(\gamma t/3\). Then (18) excludes every other slope, while the
nonzero correction excludes \(l_j\) itself. For small \(b\),
\[
                      P(\alpha+s^p,e^{\zeta_{\rm nor}})\ne0.
 \tag{24}
\]
The factor \(u'(s)\), of order \(s^{p-1}\), is essential in
(20). It changes the \(O(\delta t^p)\) radial derivative into
an \(O(\delta t)\) perturbation, still below the true slope gap.
The full actual symbol, including its unit factor, is tested.

## 4. Nested profiles with radial and angular end collars

Enlarge the desired angular rectangle by fixed positive margins.
Choose a smooth cutoff \(0\le\psi(\sigma,\theta)\le1\), equal to
one on that rectangle and zero near both ends of each enlarged
interval. Its first derivatives can be bounded by an absolute
constant after taking margins at least one.

Fix a target in (10), with \(t_0=|s_0|<b/4\) and \(\rho_0\ne0\).
Choose \(a<t_0/4\) and \(\varepsilon>0\) so small that
\[
                 \delta(3a+\varepsilon b)^\omega<|\rho_0|/2.
 \tag{25}
\]
There is a smooth increasing function \(\phi\) on \([a,b]\)
with the following elementary properties:
\[
 \begin{gathered}
 0<\phi\le t,\qquad 0<\phi'\le K_2,\qquad
 \phi=t\ \hbox{near }a\hbox{ and }b,\\
                         \phi(t_0)\le3a+\varepsilon b.
 \end{gathered}
 \tag{26}
\]
For an explicit construction, keep derivative one through \(2a\),
decrease it smoothly to \(\varepsilon\) on \([2a,3a]\), and keep
that derivative afterward. Call this function \(\phi_{\rm flat}\).
Then set
\(\phi=t-(t-\phi_{\rm flat})\chi(t)\), where \(\chi=1\) through
\(b/2\), \(\chi=0\) from \(3b/4\), \(\chi'\le0\), and
\(|\chi'|\le K/b\).
Direct differentiation gives (26) with a universal \(K_2\).

For \(0\le\lambda\le1\) put
\[
 r_\lambda(t,\sigma,\theta)
  =\delta\{(1-\lambda\psi)t^\omega
                         +\lambda\psi\phi(t)^\omega\}.
 \tag{27}
\]
These profiles decrease with \(\lambda\) and equal
\(r_0=\delta t^\omega\) near all radial and angular ends.
Moreover
\[
 \begin{split}
 (r_\lambda)_t
  &=\delta\omega\{(1-\lambda\psi)t^p
                           +\lambda\psi\phi^p\phi'\}>0,\\
 |(r_\lambda)_t|+|(r_\lambda)_\sigma|/t
  &\le K_3\delta t^p .
 \end{split}
 \tag{28}
\]
The fixed \(K_3\) depends only on \(p,K_2\) and the cutoff derivative
bound. Choose the \(\delta\) in Section 3 using this value.
No bound on \(r_\theta/r\) independent of the target is needed.
For each chosen target it is finite on the compact box.

On the finite angular cover define
\[
 \Omega_\lambda=
 \left\{a<|s|<b,\quad
  r_\lambda(|s|,\sigma,\theta)<|\rho|<2\delta|s|^\omega\right\},
 \tag{29}
\]
with the enlarged angular intervals. These domains are nested.
The source is known on \(\Omega_0\) by (15), including buffered
collars. Near every radial or angular end the moving profile agrees
with \(r_0\). The outer radial boundary also stays in the known
annulus. Thus the only moving boundary has compact support in
the interior of this radial-angular box.
Every point of it satisfies (24). The target lies in \(\Omega_1\).

## 5. Actual extension through the whole homotopy

Apply [E, Section 7] to the actual source and companions at the
moving boundary of (29). At every boundary point \(s\ne0\), (3)
is a local analytic change of meridian coordinate, so that (20)
is exactly the covector tested by that theorem.

Here is the continuation and gluing argument. Suppose there were a
first stopping parameter \(\lambda_*\). The compatible earlier
extensions define a holomorphic source and its companions on the
full known side of the boundary of \(\Omega_{\lambda_*}\).
Where the profile changes, the union of earlier domains is precisely
that known side; where it does not change, the original buffered
collars are available.
Each interior base point is reached by a finite continuation chain
from the original outer branch. This supplies the actual base
histories required by [E].

The boundary is \(C^2\), has nonzero \(\xi\)-normal, and obeys (24).
The local theorem therefore extends the source and all its companions
across each point. Its shrinking-slab proof uses meridian radius
\(O(\sqrt\epsilon)\) and primitive length \(O(\epsilon)\) in the
original local \(u\)-coordinate. The convergence condition is
\(O(\sqrt\epsilon)\), independently of the finite source-history norm.
The local coefficient constants may depend on the point and target;
no estimate uniform as \(s\to0\) is needed in this compact annulus.

Take a finite family of extension patches over the moving compact
boundary. Refine them so that relevant overlaps meet the connected
known side. Analytic uniqueness glues their source and companion
extensions. Together with the fixed end and outer collars, these
patches allow a positive further change in \(\lambda\), or include
the final boundary if \(\lambda_*=1\). This contradicts first stopping.
The entire homotopy is therefore reached.

All this takes place on the specified angular cover. Its finite
window domains are contractible radial boxes, so there is no demand
that the source return after a finite number of turns. If several
targets are used, their radial domains intersect in connected radial
domains containing the same known outer collar. Uniqueness gives
agreement there. Enlarging angular windows gives the same agreement
where their continued outer branches agree. A different outer
continuation word is retained as a possibly different branch.

Taking the union over targets proves (10). For each nonzero target
the argument used one compact \(s\)-annulus and one finite angular
window, not an infinite succession of shrinking meridian buffers.
It does not prove a common \(s\)-radius on the entire infinite cover.

## 6. Exact nonremovable partner support

Choose the canonical exceptional pair at \(\eta_j^*\).
On a fixed small annulus about that point, the two branches of the
exceptional profile in [J] differ nontrivially. Choose a basepoint
there at which their difference is nonzero. Joint continuation in
[J] makes the corresponding difference holomorphic in \(s\) near
zero and nonzero for all sufficiently small \(s\).

The center \(\eta_j(s)\) differs from \(\eta_j^*\) by \(O(s)\).
For small \(s\), a circle about the exact center within the buffered
annulus is homotopic to the original exceptional circuit, with its
chosen access path and basepoint. Under (14) this is a loop about
\(\rho=0\). Multiplication by \(s^{-p}\) does not change nonvanishing
at \(s\ne0\). The continuation of Section 5 preserves this loop
and its original histories.

If this branch were removable as a single-valued holomorphic
function through \(\rho=0\), its small-loop monodromy would be
trivial. Analytic uniqueness on the continued punctured cluster
would contradict the nonzero outer difference. Thus (11) is
nonremovable for this canonical pair, while (10) excludes additional
support in that local punctured cluster.

There is also a source-intrinsic classical consequence. If another
actual finite-shift annihilator has coefficients holomorphic on the
same local chart, its classical symbol \(Q_{\rm cl}\) satisfies
\[
                    Q_{\rm cl}(\alpha+s^p,\ell_j(s))=0.
 \tag{30}
\]
Otherwise at one \(s_0\ne0\) the boundary \(\operatorname{Re}\rho=0\)
would be noncharacteristic for that operator, with normal ratio
\(S_j'(s_0)/u'(s_0)=l_j(s_0)\).
Section 5 supplies its one-sided source branch and all companions;
[E] would extend it through \(\rho=0\), contradicting its monodromy.
The identity extends in \(s\) across zero.
The argument retains the whole actual operator and establishes
classical branch vanishing only, not a quantum right-factor identity.

## 7. What has not been extended

The cluster neighborhoods are disjoint from \(\xi=0\) and from the
other action curves when \(\delta\) and \(b\) have been chosen as above.
Thus the argument does not test removal of \(\xi=0\) after a partner
monodromy. The Euler factor in [J]'s transverse system allows
additional origin behavior on continued sheets unless a separate
source calculation excludes it.

Likewise [J] supplies bounded-\(\eta\) joint charts, not a uniform
fixed-\(\xi\) outer domain through \(s=0\). We have not obtained
such a domain by this argument. In particular (10) is a conic local
cluster statement with the finite-window convention stated above.

No order-two monodromy at nonzero \(s\), finite Laurent principal
part, convergent regular square-root amplitude, Borel growth at
infinity, physical Laplace comparison, or geometric character
identification is asserted. Nonzero exceptional fold monodromy
and local exact action support do not alone imply these statements.

## 8. Complete proof sources and coverage

| Label | Complete proof source | SHA256 |
|---|---|---|
| J | notes/research_classical_verma_higher_collision_joint_continuation.md | e2a9c50201d464a45a5359d9d8654ef18ab196d06e72c2c95c18a7aa58e0698c |
| E | notes/research_actual_borel_analytic_elliptic_inverse.md | d84ffc6794bd05917168595ec909fcb739e693b7c7574dea7471a404fa328e55 |

Both complete texts were read in full and their used implications
checked. J supplies the actual canonical ramified source, finite-path
joint continuation, and its nonzero exceptional monodromy. E supplies
the exact-source noncharacteristic extension with all companions.
The ramified classical division, angular normal, nested profiles,
cover bookkeeping and local support conclusion are proved above.

The complete earlier simple-node moving-divisor note was read for
coverage. It uses a separately proved fixed-\(\xi\), twofold outer
resolution; neither that stronger outer domain nor its deck relation
is assumed here. Its radial construction is rederived with both
angular ends retained, so no smoothness theorem for unknown singular
support is imported.

Only written mathematics, source reads and hash checks were used.
Frozen proofs and public manuscripts are unchanged.
