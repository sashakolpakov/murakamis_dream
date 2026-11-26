# Joint Borel continuation at a higher abelian collision

Private written proof, 18 November 2026.

The ramified canonical germ of [H] continues jointly along every fixed
finite Borel path avoiding its exceptional critical points and zero.
The proof retains the full finite-shift source. Its leading equation
is inverted using scaled primitives, so no high derivative of the
lower transverse forcing is introduced.

This gives nonzero monodromy of the actual Borel germ at small nonzero
ramification parameter. It does not locate a moving singular divisor,
prove a regular minor there, or identify a physical scalar coefficient.

## 1. Actual source and assertion

Keep the source, actual operator and hypotheses of [H]. In particular,
\[
 h=\log Q,\qquad
 \mathscr W(h,Y)=\sum_{j\ge0}h^jW_j(Y),\qquad
 W_0=\Delta(Y)^{-1},
 \tag{1}
\]
and \(\alpha\ne0,1\) is a simple Alexander root. The displayed actual
annihilator is
\[
 \mathcal P_h=\sum_{i\in\mathcal I}p_i(h,Y)T^i,\qquad
 Tf(Y)=f(e^hY),\qquad
 P(Y,L)=\sum_i p_i(0,Y)L^i,
 \tag{2}
\]
with a finite set \(\mathcal I\subset\mathbb Z\), holomorphic
coefficients near \((0,\alpha)\), and the original left ordering.
For a fixed integer \(p\ge1\), assume exactly
\[
 \begin{split}
 &P(Y,1)\equiv0,\qquad P_{YL}(\alpha,1)\ne0,\\
 &\partial_L^aP(\alpha,1)=0\quad(2\le a\le p),\qquad
 \partial_L^{p+1}P(\alpha,1)\ne0 .
 \end{split}
 \tag{3}
\]
The vanishing range is empty for \(p=1\). Put
\[
 \omega=p+1,\quad
 r=\Delta'(\alpha)^{-1},\quad
 B=\alpha P_{YL}(\alpha,1),\quad
 C=\frac{\alpha^{p+1}}{(p+1)!}\partial_L^{p+1}P(\alpha,1),
 \quad \kappa=(-1)^{p+1}C/B .
 \tag{4}
\]
These constants are nonzero. The actual source transport in [H]
forces \(P_L(\alpha,1)=0\) and the first subprincipal value \(B\).

The jointly holomorphic initial germ already proved in [H] is
\[
 b(s,\eta)
   =s^p\mathcal B_h\mathscr W(\alpha+s^p,s^{p+1}\eta)
   =\sum_{j\ge0}s^{p+(p+1)j}W_j(\alpha+s^p)\frac{\eta^j}{j!}.
 \tag{5}
\]
Write \(b(s,\eta)=\sum_{k\ge0}b_k(\eta)s^k\).
Its exceptional restriction is
\[
 b_0(\eta)=r\frac{U(t)}{(p+1)-pU(t)},\qquad
 U=1+tU^{p+1},\quad U(0)=1,\quad
 t=\frac{\kappa\eta^p}{p+1}.
 \tag{6}
\]
Let
\[
 \Sigma_p=\left\{\eta:
       \eta^p=\frac{p^p}{(p+1)^p\kappa}\right\}.
 \tag{7}
\]

**Theorem.** Start in (5) and subsequently follow any fixed finite
piecewise smooth path in
\(\mathbb C\setminus(\{0\}\cup\Sigma_p)\).
The source continues jointly holomorphically near that path and
\(s=0\). The allowed \(s\)-radius can decrease with the path, but is
strictly positive for every such fixed path.

For each exceptional critical point there is a based loop obtained
from the canonical radial approach to it, a small local circuit, and
return. At a sufficiently small nonzero basepoint, the continued
minus original germ has a nonzero value at \(s=0\), and consequently
is nonzero for every sufficiently small \(s\), including \(s\ne0\).

Continuation on another sheet is not asserted to be removable at
\(\eta=0\). The assertion concerns this canonical ramified Borel
source and not an independently chosen solution of its equation.

## 2. Exact finite shifts and transverse weights

Put \(z=Y-\alpha\). Taylor expansion of the actual finite shifts gives
\[
 \mathcal P_h=\sum_{n\ge1}h^n\sum_{\ell=0}^n
                    a_{n\ell}(z)\partial_z^\ell,
 \tag{8}
\]
where the order-zero differential operator vanishes. Explicitly,
\[
 \sum_{n\ge0}h^n a_{n\ell}(z)
  =\frac1{\ell!}\sum_{i\in\mathcal I}
       p_i(h,\alpha+z)
       [(\alpha+z)(e^{ih}-1)]^\ell.
 \tag{9}
\]
Here \(i\) is the integer shift index, not the imaginary unit.
For \(\ell>0\), the right side has order at least \(\ell\) in \(h\).
On fixed smaller coefficient disks, \(|e^{ih}-1|\le K|h|\)
uniformly over the finite index set. Cauchy's estimates in \(h,z\)
therefore give constants \(K_0,H,Z>0\), independent of all indices,
such that
\[
       |[z^v]a_{n\ell}|\le \frac{K_0H^nZ^v}{\ell!}.
 \tag{10}
\]
The displayed factorial is retained below.

Set
\[
 z=s^p,\qquad h=s^{p+1}\varepsilon,\qquad
 \phi=s^p\mathscr W,\qquad
 \mathcal E=s\partial_s-(p+1)\varepsilon\partial_\varepsilon.
 \tag{11}
\]
Differentiation at fixed \(h\) gives the exact identity
\[
 \partial_z^\ell(s^{-p}\phi)
  =p^{-\ell}s^{-p(\ell+1)}
        \Pi_\ell(\mathcal E)\phi,\qquad
 \Pi_\ell(t)=\prod_{a=1}^{\ell}(t-ap).
 \tag{12}
\]
For comparison, an individual original shift on the punctured chart
uses
\[
 s_i^p=s^p+(\alpha+s^p)(e^{ih}-1),\qquad
 \varepsilon_i=h/s_i^{p+1},\qquad
 T^i\mathscr W=s_i^{-p}\phi(s_i,\varepsilon_i),
 \tag{13}
\]
with the branch \(s_i=s\) at \(h=0\).
Equations (9) and (12) are precisely its fixed-\(h\) Taylor expansion.
We do not assume that the separate roots in (13) are holomorphic at
\(s=0\).

After division of \(\mathcal P_h\mathscr W=0\) by
\(s\varepsilon=h s^{-p}\), its term indexed by \(n,\ell,v\) is
\[
 p^{-\ell}[z^v]a_{n\ell}\,
       s^{\rho}\varepsilon^{n-1}\Pi_\ell(\mathcal E)\phi,
 \qquad
 \rho=(p+1)(n-1)-p\ell+pv .
 \tag{14}
\]
Every nonzero term has \(\rho\ge0\). The complete zero-weight part is
\[
       \frac Bp\mathcal E
       +\frac{C}{p^{p+1}}\varepsilon^p\Pi_{p+1}(\mathcal E).
 \tag{15}
\]

Here are all the possible borderline terms. By [H],
\[
 a_{11}=Bz+O(z^2),\qquad a_{10}=B+O(z),\qquad
 a_{p+1,p+1}=C+O(z).
 \tag{16}
\]
The first two combine to
\((B/p)(\mathcal E-p)+B=(B/p)\mathcal E\).
For \(2\le n\le p\), the top coefficient \(a_{nn}(0)\) vanishes.
Its terms thus have \(v\ge1\) and \(\rho\ge n-1\).
Terms with \(\ell\le n-1\) in this range also have \(\rho\ge n-1\).
For \(n\ge p+1\), one has \(\rho\ge n-p-1\), with equality
zero only at \(n=\ell=p+1,v=0\).
For \(n=1\), (16) accounts for the only zero weights and removes the
apparent negative weight. These observations prove (15).

Every remaining source term has an integer \(\rho\ge1\), and
\[
             n\le\rho+p+1,\qquad pv\le\rho+p.
 \tag{17}
\]
Thus only finitely many original terms occur at each transverse
degree. No high normal-order tail is discarded in (14).

## 3. Leading equation and a primitive companion system

Let \(I\) denote integration from zero, initially in the canonical
germ and subsequently along its actual continuation path. Set
\(\theta=\eta\partial_\eta\).
Borel transformation in \(\varepsilon\) sends
\(\varepsilon^a\) to \(I^a\) and
\(\varepsilon\partial_\varepsilon\) to \(\theta\).
Write \(c=C/p^{p+1}\).
Since
\(\mathcal E\varepsilon^p
 =\varepsilon^p(\mathcal E-p(p+1))\),
the leading operator on the coefficient of \(s^k\) factors as
\[
 (k-\omega\theta_\varepsilon)
       \left[\frac Bp+c\varepsilon^p
                      \Pi_p(k-\omega\theta_\varepsilon)\right].
 \tag{18}
\]
Define
\[
 G_k=\frac Bp b_k+c I^p\Pi_p(k-\omega\theta)b_k.
 \tag{19}
\]
The full coefficient equation is exactly
\[
                      (k-\omega\theta)G_k=F_k,
 \tag{20}
\]
where \(F_k\) is minus all the positive-weight terms in (14).
It involves only \(b_j\) with \(j<k\), and \(F_0=0\).

The second part of (19) can be normal-ordered without differentiating
\(F_k\). The identity \(I^p\theta=(\theta-p)I^p\) gives
\[
 I^p\Pi_p(k-\omega\theta)
 =\Pi_p(k+\omega p-\omega\theta)I^p
 =\sum_{\nu=0}^p d_\nu(k)\eta^\nu I^{p-\nu},
 \tag{21}
\]
where
\[
 d_\nu(k)=\frac1{\nu!}\Delta_t^\nu
       \Pi_p(k+\omega p-\omega t)\big|_{t=0}.
 \tag{22}
\]
Thus \(d_\nu\) has \(k\)-degree at most \(p-\nu\), and
\(d_p=(-\omega)^p\). In particular
\[
 G_k=D_p(\eta)b_k+\sum_{a=1}^p Q_a(k,\eta)I^a b_k,
 \tag{23}
\]
where
\[
 \begin{split}
 D_p(\eta)&=\frac Bp+c(-\omega)^p\eta^p
       =\frac Bp\left[1-\kappa
                         \left(\frac{p+1}{p}\right)^p\eta^p\right],\\
 Q_a(k,\eta)&=c\,d_{p-a}(k)\eta^{p-a},
                  \qquad \deg_k Q_a\le a .
 \end{split}
 \tag{24}
\]
The zeros of \(D_p\) are precisely (7), all simple.

Put \(\lambda_k=k+1\), and retain the \(p+1\) unknowns
\[
             G_k,\qquad X_{a,k}=\lambda_k^a I^a b_k
                                \quad(1\le a\le p).
 \tag{25}
\]
On a path avoiding zero and \(\Sigma_p\), recover
\[
 b_k=D_p^{-1}
       \left(G_k-\sum_{a=1}^p
                    \frac{Q_a(k,\eta)}{\lambda_k^a}X_{a,k}\right).
 \tag{26}
\]
All coefficients here, and their first \(\eta\)-derivatives, are
bounded independently of \(k\) on compact path neighborhoods.
Equations (20) and (25) give a first-order system:
\[
 \begin{split}
 G_k'&=\frac{k}{\omega\eta}G_k-\frac{1}{\omega\eta}F_k,\\
 X_{1,k}'&=\lambda_k b_k,\\
 X_{a,k}'&=\lambda_k X_{a-1,k}\quad(2\le a\le p).
 \end{split}
 \tag{27}
\]
Its matrix is bounded by a constant times \(k+1\); its forcing
coefficient is bounded independently of \(k\).
The only finite singularities of this system are zero and (7).

The primitive initial values in (25) are prescribed by the original
germ. With those values, (27) preserves \(X_{a,k}=\lambda_k^a I^a b_k\);
then (26) preserves (19). Equation (20) is retained without
differentiating it. Hence neither this system nor its continuation
loses a primitive constant or adds a freely chosen solution.

## 4. Exact lower forcing and its factorial budget

A positive-weight term of (14), with \(j=k-\rho\ge0\), contributes
to \(F_k\) a scalar multiple of
\[
 p^{-\ell}[z^v]a_{n\ell}\,
       I^{n-1}\Pi_\ell(j-\omega\theta)b_j .
 \tag{28}
\]
Put \(a=n-1\). Exact normal ordering gives
\[
 I^a\Pi_\ell(j-\omega\theta)
 =\Pi_\ell(j+\omega a-\omega\theta)I^a
 =\sum_{\nu=0}^{\ell}
                d_\nu(j,a,\ell)\eta^\nu I^{a-\nu}.
 \tag{29}
\]
Here \(I^0=1\) and \(I^{-1}=\partial_\eta\). Since
\(\ell\le n=a+1\), there is no higher negative primitive.
The finite-difference formula and bound are
\[
 \begin{split}
 d_\nu(j,a,\ell)
   &=\frac1{\nu!}\Delta_t^\nu
       \Pi_\ell(j+\omega a-\omega t)\big|_{t=0},\\
 \frac{|d_\nu(j,a,\ell)|}{\ell!}
   &\le
     \frac{\omega^\nu(j+C_p n)^{\ell-\nu}}
          {\nu!(\ell-\nu)!}.
 \end{split}
 \tag{30}
\]
To prove the inequality, express the finite difference as an integral
of the \(\nu\)-th derivative over \([0,1]^\nu\).
The product derivative has
\(\nu!\binom{\ell}{\nu}\) terms, each with \(\nu\) factors
\(-\omega\). All remaining factors are bounded by \(j+C_p n\).
This proves (30) after division by \(\nu!\ell!\).

The normal ordering is valid for the full continued primitives.
Expansion in the falling powers of \(\theta\) uses
\(\theta^{\underline{\nu}}=\eta^\nu\partial_\eta^\nu\), and
\(\partial_\eta^\nu I^a=I^{a-\nu}\).
For the possible endpoint \(\nu=a+1\) the latter is the first
derivative. There is no integration-by-parts boundary term to omit.

Fix a finite path as in the theorem, preceded by a short path from
zero inside the known germ. Parameterize it by arc length
\(t\in[0,T]\), including that initial segment, so \(\eta(0)=0\).
Choose a later time \(t_*>0\) in the known germ, with
\(\eta(t_*)\ne0\), as the initial point for (27).
The remaining compact path \(t\in[t_*,T]\) has positive distance
from zero and \(\Sigma_p\). Put
\(R=\max(1,\sup|\eta(t)|)\). For \(\Lambda\ge1\), define
\[
 M_j=\sup_{0\le t\le T}e^{-\Lambda(j+1)t}
       \max\left(|b_j(\eta(t))|,
                       \frac{|b_j'(\eta(t))|}{j+1}\right).
 \tag{31}
\]
For every integer \(u\ge1\), the exact full-path primitive is
\[
 I^u b_j(\eta(t))
  =\frac1{(u-1)!}\int_0^t
      [\eta(t)-\eta(v)]^{u-1}b_j(\eta(v))\eta'(v)\,dv.
 \tag{32}
\]
This formula follows by differentiation with its zero initial value
and remains valid for paths with loops. Since
\(|\eta(t)-\eta(v)|\le t-v\),
\[
 \sup_t e^{-\Lambda(j+1)t}|I^u b_j(\eta(t))|
                  \le [\Lambda(j+1)]^{-u}M_j .
 \tag{33}
\]
For \(u=0\) the bound is \(M_j\); for \(u=-1\) it is
\((j+1)M_j\).

For \(\nu\le a\), combining (10), (28)--(30), and (33) bounds one
term, in the output weight \(k\ge j\), by
\[
 K_0H^nZ^v p^{-\ell}
 \frac{\omega^\nu R^\nu(j+C_p n)^{\ell-\nu}}
      {\nu!(\ell-\nu)!}
 [\Lambda(j+1)]^{-(n-1-\nu)}M_j .
 \tag{34}
\]
The remaining power of \(j+1\) is at most
\(\ell-n+1\le1\). With \(w=\ell-\nu\),
\[
 \frac{(1+C_p n/(j+1))^w}{w!}
                     \le e^{1+C_p n}.
 \tag{35}
\]
The sum over \(\nu\) and all other fixed factors in (34) are
therefore at most an exponential in \(n+v\), times \((j+1)M_j\).
For \(\nu=a+1\), necessarily \(\nu=\ell=n\), and its bound is
\[
 K_0H^nZ^v p^{-n}\frac{(\omega R)^n}{n!}(j+1)M_j,
 \tag{36}
\]
with the same conclusion.

The relations (17) bound \(n+v\) by a fixed multiple of \(\rho+1\).
At each \(\rho\), the number of triples \(n,\ell,v\) is polynomial
in \(\rho+1\). Absorbing that count into an exponential yields
\[
 \|F_k\|_k:=
   \sup_t e^{-\Lambda(k+1)t}|F_k(\eta(t))|
       \le K_1\sum_{\rho=1}^k
                  D^\rho(k-\rho+1)M_{k-\rho}.
 \tag{37}
\]
This is the full actual forcing. The estimates do not drop terms
of large normal order; their number at every fixed \(k\) is finite.

## 5. Inverting the leading system and summing the transverse jets

On the compact subpath \(t\in[t_*,T]\), (27) has matrix norm
at most \(K_2(k+1)\) and forcing norm at most \(K_2|F_k|\).
This includes the bounds from (26). Choose
\(\Lambda>K_2+1\).
The integral equation for a linear system gives its fundamental
matrix norm at most \(e^{K_2(k+1)|t-v|}\):
iterate its integral equation, and sum
\(\sum_{n\ge0}(K_2(k+1)|t-v|)^n/n!\).
Consequently its forced solution has weighted norm at most
\[
                         \frac{K_3}{k+1}\|F_k\|_k.
 \tag{38}
\]
Formula (26) gives the same bound for \(b_k\).
Differentiating (26) once and using (27) bounds
\(b_k'/(k+1)\) by a constant times the state plus
\(|F_k|/(k+1)\). Thus (38) controls both entries of (31).
In particular no derivative of \(F_k\) is used.

The known joint germ (5) bounds \(b_k\) and \(b_k'\) by
\(K_4D_0^k\) on a fixed smaller initial \(\eta\)-disk.
Its primitives at the initial point have the same exponential
bound. The \(X_{a,k}\) initial values multiply this only by
\((k+1)^a\), \(a\le p\).
Equations (23)--(24) give the same bound, times a fixed polynomial
in \(k\), for \(G_k\). These polynomial factors can be absorbed
into a fixed exponential in \(k\).
Their homogeneous propagation in (27), with the weight (31),
retains such a bound.

Combining the initial data, (37), and (38) proves
\[
 M_k\le K_5D_1^k+
                 K_5\sum_{\rho=1}^kD^\rho M_{k-\rho}.
 \tag{39}
\]
This recurrence has an exponential majorant. For example choose
\(D_2>D_1,D\) so large that
\(K_5\sum_{\rho\ge1}(D/D_2)^\rho<1/2\);
then induction with a sufficiently large prefactor gives
\(M_k\le K_6D_2^k\).
Removing the path weight yields
\[
 \sup_t\left(
 |b_k(\eta(t))|+\frac{|b_k'(\eta(t))|}{k+1}\right)
                    \le K_7(D_2e^{\Lambda T})^k .
 \tag{40}
\]

First continue each coefficient inductively: lower coefficients and
their path primitives define \(F_k\), and the ordinary system (27)
continues its prescribed initial data. Estimate (40) then makes
\(\sum_k b_k(\eta)s^k\) normally convergent for a positive \(s\)-radius.
Cover the path by finitely many small disks avoiding the punctures
and use nearby paths in the same successive charts. Their lengths,
distances from the punctures, and \(|\eta|\)-bounds can be chosen
uniformly. The same estimate holds on those neighborhoods.
The summed series is jointly holomorphic there and agrees with (5)
initially. It is therefore the continuation of that actual germ.

## 6. Nonzero nearby monodromy

Fix one point \(\eta_c\in\Sigma_p\). Under
\(t=\kappa\eta^p/(p+1)\), lift the positive real approach
\(0<t<t_*=p^p/(p+1)^{p+1}\) to its radial approach.
The branch \(U(0)=1\) reaches \(U_*=(p+1)/p\).
As proved in [H], \(t\) has a nondegenerate critical point there,
and the exceptional profile has a nonzero inverse-square-root
singularity. A small circuit interchanges this branch with the
other local branch.

Return along the radial path to a sufficiently small nonzero
basepoint \(\eta_b\). The returned \(U\)-branch is different from
the original one. Indeed the critical point is a simple fold.
As \(t\to0\), the only bounded root of \(U=1+tU^{p+1}\) is its
unique root near one; all the other roots tend to infinity.
The returned branch thus satisfies
\[
 \frac{U}{(p+1)-pU}\longrightarrow-\frac1p,
 \qquad
 \frac{U_{\rm original}}{(p+1)-pU_{\rm original}}
                         \longrightarrow1.
 \tag{41}
\]
The two exceptional values differ by a quantity tending to
\(-r(p+1)/p\ne0\).
Choose the basepoint small enough that this difference is nonzero.
This specifies a finite based loop avoiding zero and the other
critical points.

By the joint continuation just proved, its continued-minus-original
value is holomorphic in \(s\) near zero. Its value at \(s=0\) is
the nonzero difference in (41). It remains nonzero throughout a
sufficiently small \(s\)-disk. This is nontrivial monodromy of the
actual source at nonzero \(s\), not merely of the restriction (6).
It does not specify where the singular set lies at that nonzero
\(s\), or permit return through \(\eta=0\) on every sheet.

## 7. Complete source and scope

The sole proof direct, read completely with its used implications
checked, is:

| Label | Complete proof source | SHA256 |
|---|---|---|
| H | notes/research_classical_verma_higher_collision_borel_profile.md | 09de4f17620c4bed52b7382325c2b9bd54b8c9b50ed62cd61e31953bba5d6838 |

H supplies the actual finite-shift source, the collision transport
and vanishing coefficients in (16), the jointly holomorphic initial
ramified germ, and its algebraic exceptional profile.
All normal ordering, companion-system estimates, path histories,
and joint continuation arguments are proved here.
The complete earlier note
notes/research_classical_verma_borel_joint_continuation.md was read
for coverage: it proves the \(p=1\) result. Its method is rederived
above, with a primitive companion of dimension \(p+1\); it is not
an additional proof premise.

If the original supplied operator annihilates
\((Y-1)\mathscr W\), its actual composition with multiplication by
\(Y-1\) is retained as in H. No scalar right factor is substituted
for the source operator. Negative shifts are included in (9).
No analytic theorem about general resurgence or propagation of
singularities is imported.

No Borel growth at infinity, Laplace realization, moving-divisor
location, regular moving minor, marked-character continuation,
geometric component identification, or physical scalar lower bound
is asserted. The collision hypotheses remain explicit conditions on
the actual operator, not a claim covering every Alexander attachment
or every short filling.

Only written mathematics, source reads and hash checks were used.
Frozen proofs and public manuscripts are unchanged.
