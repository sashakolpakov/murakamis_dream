# Joint continuation of the canonical pole-scaled Borel source

This private note continues the actual canonical Borel germ of [C].
The proof uses the factorials in the finite quantum shifts and the
Volterra integrals together. It proves continuation near the exceptional
divisor and nonzero nearby Borel monodromy. It does not identify a
Laplace sum, a geometric branch, or the original large-level scalar.

## 1. Source, hypotheses, and assertion

Use the original natural meridian and parameter of [C]:

\[
 h=\log Q,\qquad
 \mathscr W(h,Y)=\sum_{j\ge0}h^jW_j(Y),\qquad W_0(Y)=\Delta_K(Y)^{-1}.
 \tag{1}
\]

Let \(\alpha\ne0,1\) be a simple Alexander root. Suppose a supplied
actual finite-shift annihilator, in left coefficient ordering, is

\[
 \mathcal P=\sum_{\nu\in J}p_\nu(h,Y)T^\nu,
 \qquad T f(Y)=f(e^hY),\qquad \mathcal P\mathscr W=0,
 \tag{2}
\]

where \(J\subset\mathbb Z\) is finite and the coefficients are
holomorphic near \((0,\alpha)\). Write
\(P(Y,L)=\sum_\nu p_\nu(0,Y)L^\nu\). Retain exactly the node hypotheses
of [C]:

\[
 P(Y,1)\equiv0,\quad P_L(\alpha,1)=0,\quad
 P_{LL}(\alpha,1)P_{YL}(\alpha,1)\ne0.
 \tag{3}
\]

Set

\[
 z=Y-\alpha,\quad
 r=\Delta_K'(\alpha)^{-1},\quad
 A=\tfrac12\alpha^2P_{LL}(\alpha,1),\quad
 B=\alpha P_{YL}(\alpha,1),\quad \eta_*={B\over2A}.
 \tag{4}
\]

The canonical germ proved in [C] is

\[
 b(z,\eta)=\sum_{j\ge0}z^{2j+1}W_j(\alpha+z){\eta^j\over j!},
 \qquad b(0,\eta)=r(1-\eta/\eta_*)^{-1/2}.
 \tag{5}
\]

Its branch at \(\eta=0\) has value \(r\).

**Theorem.** Start in the germ (5), and subsequently follow any finite
piecewise smooth path in \(\mathbb C\setminus\{0,\eta_*\}\).
The germ continues jointly holomorphically near that path and \(z=0\).
For every such fixed path there is a positive, possibly smaller,
\(z\)-radius on which the continued Taylor series in \(z\) converges
normally on a finite collection of neighborhoods along the path.

If a loop based at a small nonzero \(\eta_b\) winds once around
\(\eta_*\) and not around zero, its continued-minus-original germ at
\(\eta_b\) is nonzero for every sufficiently small \(z\), including
\(z\ne0\). Its value at \(z=0\) is

\[
                 -2r(1-\eta_b/\eta_*)^{-1/2}\ne0.
 \tag{6}
\]

No removability at \(\eta=0\) is asserted after continuation to another
sheet. A normal-state operator annihilating \((Y-1)\mathscr W\) is
handled exactly as in [C] by composing on the right with \(Y-1\).
At \(\alpha\ne1\) this changes neither \(A/B\) nor the argument.

## 2. Exact shift expansion and its factorial estimate

Taylor expansion at fixed \(h\) gives

\[
 \mathcal P=\sum_{n\ge1}h^n\sum_{\ell=0}^n
                  a_{n\ell}(z)\partial_z^\ell,
 \tag{7}
\]

with zero order-zero operator. More precisely,

\[
 \sum_{n\ge0}h^n a_{n\ell}(z)
  ={1\over\ell!}\sum_{\nu\in J}p_\nu(h,\alpha+z)
           [ (\alpha+z)(e^{\nu h}-1)]^\ell.
 \tag{8}
\]

For \(\ell=0\), the coefficient of \(h^0\) vanishes by (3).
For \(\ell>0\), (8) vanishes to order at least \(\ell\) in \(h\).
Choose fixed smaller \(h,z\) disks. The finite set of shifts satisfies
\(|e^{\nu h}-1|\le C|h|\) there, and all \(p_\nu\) are bounded.
Cauchy's estimates in both variables, absorbing constants raised to
\(\ell\le n\), give constants \(C,H,Z\), independent of the indices,
such that

\[
       |[z^v]a_{n\ell}(z)|
                   \le {C H^n Z^v\over\ell!}.
 \tag{9}
\]

This is the actual finite-shift factorial. Replacing it by a bound
without \(\ell!\) would not prove the theorem below.

Put \(h=z^2\varepsilon\), \(\phi=z\mathscr W\), and
\(E=z\partial_z-2\varepsilon\partial_\varepsilon\). At fixed \(h\),

\[
 \partial_z^\ell(z^{-1}\phi)
     =z^{-\ell-1}\prod_{i=1}^{\ell}(E-i)\phi.
 \tag{10}
\]

After division of \(\mathcal P\mathscr W=0\) by \(z\varepsilon\),
its \((n,\ell)\) term is exactly

\[
 z^{2n-\ell-2}a_{n\ell}(z)\varepsilon^{n-1}
                   \prod_{i=1}^{\ell}(E-i)\phi.
 \tag{11}
\]

[C]'s actual first-order transport and node calculation give

\[
 a_{11}(z)=Bz+O(z^2),\quad a_{10}(z)=B+O(z),\quad
 a_{22}(z)=A+O(z).
 \tag{12}
\]

The apparent negative \(z\)-power in (11) is therefore removable.
The order-zero part in \(z\) is
\(BE+A\varepsilon(E-1)(E-2)\). Every remaining term has a positive
\(z\)-power. If its total shift in \(z\)-degree is \(s\ge1\), then

\[
 s=2n-\ell-2+v,\qquad n\le s+2,\qquad v\le s+1.
 \tag{13}
\]

Thus only finitely many source terms occur at each fixed \(z\)-degree.

## 3. The exact triangular Borel hierarchy

Let \(I f(\eta)=\int_0^\eta f(\xi)\,d\xi\), initially in the
canonical germ and subsequently along the same continued path.
Write \(\theta=\eta\partial_\eta\) and
\(b(z,\eta)=\sum_{k\ge0}b_k(\eta)z^k\).
The Borel transform sends multiplication by \(\varepsilon^a\) to
\(I^a\), and \(\varepsilon\partial_\varepsilon\) to \(\theta\).
Define

\[
 G_k=Bb_k+A I[(k-1-2\theta)b_k].
 \tag{14}
\]

The leading operator factors before Borel transformation as
\((k-2\theta_\varepsilon)[B+A\varepsilon(k-2\theta_\varepsilon-1)]\).
Consequently the exact coefficient equations are

\[
 (k-2\theta)G_k=F_k,\qquad
 (B-2A\eta)b_k'+A(k-1)b_k=G_k',
 \tag{15}
\]

where \(F_k\) is minus the sum of all lower-degree terms in (11).
Each such term, with \(p=k-s\ge0\), has the form

\[
 [z^v]a_{n\ell}\ I^{n-1}
        P_\ell(p-2\theta)b_p,
 \qquad P_\ell(t)=\prod_{i=1}^{\ell}(t-i),
 \tag{16}
\]

and the indices satisfy (13). In particular \(F_0=0\).

There is no lost integration constant in (15). Indeed

\[
        G_k=(B-2A\eta)b_k+A(k+1)I b_k.
 \tag{17}
\]

This holds in the initial germ; its derivative is the second equation
of (15), so it remains true under continuation with its original
initial value. The first equation is likewise the undifferentiated
leading equation. These initial values are retained below.

The normal ordering of (16) is particularly useful. Put \(a=n-1\).
Since \(I^a\theta=(\theta-a)I^a\),

\[
 I^aP_\ell(p-2\theta)
   =P_\ell(p+2a-2\theta)I^a
   =\sum_{q=0}^{\ell}d_q\eta^q I^{a-q}.
 \tag{18}
\]

Here \(I^0\) is the identity and \(I^{-1}=\partial_\eta\).
There are no other negative powers because \(q\le\ell\le n=a+1\).
Expansion in the falling powers of \(\theta\) gives

\[
 d_q={1\over q!}\Delta_t^q
       P_\ell(p+2a-2t)\big|_{t=0},\qquad
 {|d_q|\over\ell!}
 \le {2^q(p+C_*n)^{\ell-q}\over q!(\ell-q)!}.
 \tag{19}
\]

To verify the inequality, express each finite difference as an
integral of the \(q\)-th derivative over \([0,1]^q\). The derivative
of the product has \(q!\binom\ell q\) terms, each with \(q\) factors
\(-2\); all remaining factors have modulus at most \(p+C_*n\).
Division by \(q!\ell!\) proves (19).
The equality in (18) also proves directly that no endpoint jet at
zero has been discarded: \(\partial_\eta^q I^a\) is literally
\(I^{a-q}\) for \(q\le a\), and is the first derivative for \(q=a+1\).

## 4. A full-path analytic majorant

Fix a path as in the theorem. Prepend a short path from zero to a
nonzero initial point inside the known germ. Parameterize the resulting
path by arc length \(t\in[0,L]\). Its initial segment lies inside that
germ; the remaining segment has positive distance from
\(\{0,\eta_*\}\). Write \(R=\max(1,\sup_t|\eta(t)|)\).

For a constant \(\kappa>0\), use the norm

\[
 M_p=\sup_{0\le t\le L} e^{-\kappa(p+1)t}
       \max\left(|b_p(\eta(t))|,{|b_p'(\eta(t))|\over p+1}\right).
 \tag{20}
\]

For any \(u\ge1\), the continued primitive has the exact expression

\[
 I^u b_p(\eta(t))={1\over(u-1)!}
  \int_0^t[\eta(t)-\eta(s)]^{u-1}b_p(\eta(s))\eta'(s)\,ds.
 \tag{21}
\]

It remains valid for paths with loops. Since
\(|\eta(t)-\eta(s)|\le t-s\), it gives

\[
 \sup_t e^{-\kappa(p+1)t}|I^u b_p(\eta(t))|
                      \le {M_p\over[\kappa(p+1)]^u}.
 \tag{22}
\]

For \(u=0\) the bound is \(M_p\), and for \(u=-1\) it is
\((p+1)M_p\). Thus (22) includes the entire history from zero;
no separately estimated high derivative of the initial germ is needed.

Combine (9), (18), and (19). For \(q\le a=n-1\), a normal-ordered
term in (16), in the weight of the output \(k\ge p\), is bounded by

\[
 C H^n Z^v
 {2^q R^q(p+C_*n)^{\ell-q}\over q!(\ell-q)!}
 [\kappa(p+1)]^{-(n-1-q)}M_p.
 \tag{23}
\]

The power of \(p+1\) left after factoring
\(p+C_*n\le(p+1)(1+C_*n/(p+1))\) is
\(\ell-n+1\le1\). Moreover

\[
 { (1+C_*n/(p+1))^u\over u!}
 \le \exp(1+C_*n/(p+1))\le e^{1+C_*n}.
 \tag{24}
\]

The sum over \(q\) in (23) therefore costs at most an exponential
in \(n+v\), times \((p+1)M_p\); the constants may depend on the path
and \(\kappa\). If \(q=a+1\), necessarily \(q=\ell=n\), and the
remaining term is bounded by
\(C H^n Z^v(2R)^n(n!)^{-1}(p+1)M_p\), with the same conclusion.
Using (13) and absorbing the polynomial number of choices of
\((n,\ell,v)\) into a fixed exponential yields

\[
 \sup_t e^{-\kappa(k+1)t}|F_k(\eta(t))|
          \le C\sum_{s=1}^k D^s(k-s+1)M_{k-s}.
 \tag{25}
\]

This is the point at which the actual \(\ell!\) and the Volterra
orders jointly remove a possible factorial in the transverse index.

It remains to invert the leading equations without losing that gain.
On the path after its initial point, put \(d(\eta)=B-2A\eta\).
Equations (15) are the ordinary first-order system

\[
 {d\over d\eta}\binom{b_k}{G_k}
 =\begin{pmatrix}
 -A(k-1)/d & k/(2\eta d)\\
 0 & k/(2\eta)
 \end{pmatrix}\binom{b_k}{G_k}
 -\binom{1/(2\eta d)}{1/(2\eta)}F_k.
 \tag{26}
\]

Use the unscaled vector \((b_k,G_k)\). Its matrix is bounded by
\(C_2(k+1)\), and its forcing coefficient by \(C_2\), uniformly
on the path. Choose \(\kappa>C_2+1\). The elementary integral
inequality for its fundamental matrix gives the weighted forced
solution a bound

\[
 {C_3\over k+1}\sup_t e^{-\kappa(k+1)t}|F_k(\eta(t))|.
 \tag{27}
\]

The first row of (26) gives the same bound for
\(b_k'/(k+1)\). The initial joint germ supplies
\(|b_k|+|b_k'|\le C_4D_0^k\) on its smaller initial segment.
Formula (17) bounds its initial \(G_k\) by
\(C_4(k+1)D_0^k\), also at most an exponential in \(k\).
The homogeneous contribution of (26), in the same weight, preserves
this exponential bound. Combining (25)--(27), and increasing fixed
constants, proves

\[
             M_k\le C_5D_1^k+
                    C_5\sum_{s=1}^kD^s M_{k-s}.
 \tag{28}
\]

Induction, or the geometric-series generating function of (28), gives
\(M_k\le C_6D_2^k\). Therefore

\[
 \sup_t\bigl(|b_k(\eta(t))|+|b_k'(\eta(t))|/(k+1)\bigr)
                       \le C_7(D_2e^{\kappa L})^k.
 \tag{29}
\]

## 5. Joint continuation and monodromy

Inductively, (16) and (26) first continue each coefficient along the
path. All primitives retain the same path and the initial values
from (5). Estimate (29) makes their \(z\)-series normally convergent
in a positive disk. To obtain neighborhoods rather than only path
values, cover the fixed path by finitely many small disks avoiding
zero and \(\eta_*\), and use nearby paths in the same successive
charts. Their lengths, distances from the two punctures, and absolute
\(\eta\)-bounds are uniform. The same proof gives (29) uniformly on
these neighborhoods. The convergent sum is jointly holomorphic and
agrees with the original germ initially; hence it is its analytic
continuation. This proves the first assertion.

Apply this result to the loop in Section 1. At \(z=0\), analytic
continuation is exactly that of (5), so a single circuit about
\(\eta_*\) reverses its sign. The difference of the two joint germs
at the base point is holomorphic in \(z\) and has the nonzero value
(6) at zero. It remains nonzero on a sufficiently small \(z\)-disk.
This proves nearby nontrivial monodromy of the canonical Borel source.
It does not locate the singularities for each \(z\ne0\), or show that
their continuation paths can cross \(\eta=0\) on another sheet.

## 6. Scope and complete proof source

The theorem concerns the same canonical source as [C], under its
actual-operator transverse-node hypotheses. It is not an assertion
that those hypotheses hold on every geometric character component.
For \(z\ne0\), the source is literally
\(b(z,\eta)=z\mathcal B_h\mathscr W(\alpha+z,z^2\eta)\) initially;
the theorem continues that germ, not an independently chosen solution.

No growth estimate at infinite Borel distance, Laplace summation,
identification with a finite-color analytic source, original-cycle
intersection, or large-level lower bound is obtained. In particular
nonzero Borel monodromy is not identified with a selected geometric
coefficient of the original arbitrary-short-filling problem.

The sole proof direct is the following complete text:

| Label | Complete source | SHA256 |
|---|---|---|
| C | notes/research_classical_verma_borel_pole_profile.md | 6ba957d7a521524f370cb3bdd90ab30338bff8c13960ae6ca1825d08260c77d2 |

C supplies the canonical jointly holomorphic germ, the actual ordered
transport coefficients (12), and its exact exceptional restriction.
All continuation and majorant arguments are written above. No novelty
is claimed for general Volterra or analytic-continuation methods.
Only written mathematics and source-text reads were used; no mathematical
programs, tests, numerical calculations, or builds were run. Frozen
notes and public manuscripts are unchanged.
