# Canonical Borel profiles at higher abelian collisions

Private written proof, 18 November 2026.

The actual rational-loop source admits a ramified initial Borel chart
at any finite collision of the order specified below. Its exceptional
restriction is algebraic and has nonzero square-root singularities.
The pole bound, normalization, ramification and classical action scale
are derived from the same actual finite-shift equation.

This is an initial-germ and exceptional-profile theorem. It does not
continue the joint germ at nonzero ramification parameter, locate a
full moving singular divisor, or identify a contribution to the
physical finite-color scalar.

## 1. Original source and actual collision hypotheses

Use the original reduced, zero-framed completion from [F], in the
coordinate of [G]:
\[
 h=\log Q,\qquad q=e^{h/2},\qquad
 \mathscr W(h,Y)=\sum_{j\ge0}h^jW_j(Y),\qquad
 W_0(Y)=\Delta(Y)^{-1}.
 \tag{1}
\]
The coefficients in (1) are in \(h\), not \(1-Q\). The unconditional
parts of [F] and [G] give meromorphic rational coefficients and
\[
 W_j\in\frac{\mathbb Q[Y^{\pm1}]}{\Delta(Y)^{2j+1}},\qquad
 \sup_K|W_j|\le C_KD_K^j j!
 \tag{2}
\]
on every compact \(K\Subset\mathbb C^*\setminus\{\Delta=0\}\).
The Gevrey bound here is [G, Sections 2--3]; its optional two-branch
node hypothesis is not used.

Let \(\alpha\ne0,1\) be a simple Alexander root, and put
\[
                 z=Y-\alpha,\qquad r=\Delta'(\alpha)^{-1}\ne0.
 \tag{3}
\]
Suppose a displayed actual finite-shift operator annihilates (1):
\[
 \mathcal P_h=\sum_{i\in\mathcal I}p_i(h,Y)T^i,\qquad
 Tf(Y)=f(e^hY),\qquad
 P(Y,L)=\sum_i p_i(0,Y)L^i .
 \tag{4}
\]
Here \(\mathcal I\subset\mathbb Z\) is finite, its indices are integers,
and all coefficients are holomorphic near \((h,Y)=(0,\alpha)\).
The original left coefficient ordering and state gauge are retained.

Fix an integer \(p\ge1\). The collision hypotheses are
\[
 \begin{split}
 &P(Y,1)\equiv0,\qquad P_{YL}(\alpha,1)\ne0,\\
 &\partial_L^kP(\alpha,1)=0\quad(2\le k\le p),\qquad
                 \partial_L^{p+1}P(\alpha,1)\ne0 .
 \end{split}
 \tag{5}
\]
For \(p=1\) the vanishing range is empty. The actual source equation
will also force \(P_L(\alpha,1)=0\).
Set
\[
 B=\alpha P_{YL}(\alpha,1),\qquad
 C=\frac{\alpha^{p+1}}{(p+1)!}\partial_L^{p+1}P(\alpha,1),
 \qquad \kappa=(-1)^{p+1}C/B .
 \tag{6}
\]
All three constants are nonzero.

**Theorem.** The pole orders of the actual coefficients satisfy
\[
             \operatorname{pole}_\alpha W_j
                \le t_j:=j+\lfloor j/p\rfloor+1.
 \tag{7}
\]
For \(n\ge0\), their indicated highest coefficients are exactly
\[
 a_n:=[z^{-((p+1)n+1)}]W_{pn}(\alpha+z)
       =r\kappa^n\frac{((p+1)n)!}{(p+1)^n n!}.
 \tag{8}
\]
In particular these poles are present, not merely allowed.

After the ramification
\[
                       z=s^p,\qquad \xi=s^{p+1}\eta,
 \tag{9}
\]
the literal scaled canonical Borel series
\[
 \mathcal F_p(s,\eta)
    =s^p\mathcal B_h\mathscr W(\alpha+s^p,s^{p+1}\eta)
    =\sum_{j\ge0}s^{p+(p+1)j}
                       W_j(\alpha+s^p)\frac{\eta^j}{j!}
 \tag{10}
\]
extends jointly holomorphically near \((s,\eta)=(0,0)\).
Its exceptional restriction is
\[
 \mathcal F_p(0,\eta)
   =r\sum_{n\ge0}\binom{(p+1)n}{n}
                          \left(\frac{\kappa\eta^p}{p+1}\right)^n
   =r\,\frac{U(t)}{(p+1)-pU(t)},
 \quad t=\frac{\kappa\eta^p}{p+1},
 \tag{11}
\]
where \(U=1+tU^{p+1}\), \(U(0)=1\).
This germ has nonzero inverse-square-root singularities at the
\(p\) points
\[
                        \eta^p=\frac{p^p}{(p+1)^p\kappa}.
 \tag{12}
\]
The continuations meant in this last assertion are those of the
one-variable exceptional restriction, not of (10) at \(s\ne0\).

## 2. Actual differential coefficients at the collision

Write \(P^{[1]}(Y,L)=\sum_i[h]p_i(h,Y)L^i\).
The order-\(h\) equation of the actual source is
\[
 YP_L(Y,1)W_0'(Y)+P^{[1]}(Y,1)W_0(Y)=0 .
 \tag{13}
\]
Its possible \(z^{-2}\) term is \(-\alpha P_L(\alpha,1)r\).
Thus \(P_L(\alpha,1)=0\). Comparing the next term gives
\[
                         P^{[1]}(\alpha,1)=B.
 \tag{14}
\]
This uses the nonzero source residue. Neither relation is imposed
by a free normalization of a homogeneous solution.

Expand the literal finite shifts:
\[
 \mathcal P_h=\sum_{\nu\ge1}h^\nu L_\nu,\qquad
                         \operatorname{ord}L_\nu\le\nu .
 \tag{15}
\]
Every coefficient of \(L_\nu\) is holomorphic in \(z\).
The absent order-zero differential operator is exactly \(P(Y,1)\).
Equations (13)--(14) give
\[
                L_1=(Bz+O(z^2))\partial_z+(B+O(z)).
 \tag{16}
\]

The coefficient of \(\partial_z^\nu\) in \(L_\nu\) is
\[
       \frac{Y^\nu}{\nu!}
                     \left.(L\partial_L)^\nu P(Y,L)\right|_{L=1}.
 \tag{17}
\]
Indeed it comes only from the order-\(\nu\) shift expansion of the
order-zero coefficient \(p_i(0,Y)\); its leading derivative is
\((iY)^\nu/\nu!\). The identity
\[
 (L\partial_L)^\nu
       =\sum_{k=1}^{\nu}\left\{\begin{matrix}\nu\\k\end{matrix}\right\}
                               L^k\partial_L^k
 \tag{18}
\]
follows by induction using the ordinary product rule. Its coefficient
at \(k=\nu\) is one. It applies equally to negative shift powers,
which are holomorphic near \(L=1\).

By (5), (14), and (17)--(18), for \(2\le\nu\le p\) the top
derivative coefficient vanishes at \(z=0\). Hence \(L_\nu\) raises
a meromorphic pole order by at most \(\nu-1\) in that range.
For the next coefficient,
\[
 L_{p+1}=(C+O(z))\partial_z^{p+1}
                     +\text{terms of order at most }p.
 \tag{19}
\]
For all \(\nu\ge p+1\) the general pole-order increase is at most
\(\nu\). These statements require no assumptions on their lower
derivative coefficients.

## 3. The improved pole bound and exact multiples of \(p\)

At order \(h^{j+1}\), \(j\ge1\), the actual equation reads
\[
                L_1W_j=-\sum_{\nu=2}^{j+1}L_\nu W_{j+1-\nu}.
 \tag{20}
\]
Proceed inductively from the simple pole \(W_0\).
Let \(k=j+1-\nu\). If \(2\le\nu\le p\), the pole order of the
corresponding right-hand term is at most
\[
 t_k+\nu-1=j+1+\lfloor k/p\rfloor\le t_j.
 \tag{21}
\]
If \(\nu\ge p+1\), then \(k\le j-p\), and its order is at most
\[
 t_k+\nu=j+2+\lfloor k/p\rfloor\le t_j .
 \tag{22}
\]
The ranges can be empty; the same argument covers \(j<p\) and \(p=1\).

The rationality in (2) ensures that \(W_j\) is meromorphic with a
finite pole order. If that order were \(N>t_j\), (16) would give
a nonzero coefficient \(B(1-N)\) times its leading coefficient at
order \(z^{-N}\). Since \(t_j\ge2\) for \(j\ge1\), this multiplier
cannot vanish. It contradicts (20)--(22). This proves (7).

Now let \(j=pn\), \(n\ge1\), so \(t_j=(p+1)n+1\).
For \(2\le\nu\le p\), (21) is at most \(t_j-1\).
For \(\nu\ge p+1\), equality in (22) requires
\(\lfloor(pn+1-\nu)/p\rfloor=n-1\), which forces
\(\nu=p+1\). For that term, only the constant top derivative
in (19) reaches the indicated order. Thus there are no other
contributions to this highest pole.

The previous coefficient has exponent
\(m=(p+1)(n-1)+1\), and
\[
 \partial_z^{p+1}z^{-m}
     =(-1)^{p+1}
       \frac{((p+1)n)!}{((p+1)(n-1))!}
                                      z^{-((p+1)n+1)}.
 \tag{23}
\]
The left side of (20) contributes
\(-B(p+1)n\,a_n\). Consequently
\[
 a_0=r,\qquad
 a_n=\kappa\,
       \frac{((p+1)n)!}
            {(p+1)n\,((p+1)(n-1))!}\,a_{n-1}.
 \tag{24}
\]
Iteration gives (8), including its sign.

## 4. Convergence of the ramified canonical germ

Choose a fixed small circle \(|z|=R_0\) avoiding zero meridian,
other Alexander roots and coefficient poles, with \(R_0\le1\).
The unconditional Gevrey estimate (2) holds on this circle.
By (7), the functions
\[
                       F_j(z)=z^{t_j}W_j(\alpha+z)
 \tag{25}
\]
are holomorphic on its full disk. The maximum principle gives,
after changing constants independent of \(j\),
\[
                         \sup_{|z|\le R_0}|F_j(z)|
                                     \le C_0D_0^j j!.
 \tag{26}
\]
For example the boundary bound is
\(C_K R_0^{t_j}D_K^j j!\), and \(R_0\le1\) suffices.

If \(j=pn+r_j\), \(0\le r_j<p\), then
\[
                       p+(p+1)j-pt_j=r_j.
 \tag{27}
\]
Therefore (10) is exactly
\[
                    \mathcal F_p(s,\eta)
                   =\sum_{j\ge0}s^{r_j}F_j(s^p)\frac{\eta^j}{j!}.
 \tag{28}
\]
For \(|s|\le\min(1,R_0^{1/p})\), (26) gives a geometric majorant
in \(\eta\). Normal convergence on smaller product disks proves
joint holomorphy, including \(s=0\).
On \(s\ne0\) it is literally the scaled original Borel series;
no new coefficient family or summation is introduced.

Only indices \(j=pn\) survive at \(s=0\). Using (8),
\[
 \frac{F_{pn}(0)}{(pn)!}
          =r\binom{(p+1)n}{n}
                           \left(\frac{\kappa}{p+1}\right)^n,
 \tag{29}
\]
which proves the series in (11).

## 5. Algebraic exceptional profile and its singularities

Let \(v=U-1\). The implicit equation and its derivative are
\[
          t=\frac{v}{(1+v)^{p+1}},\qquad
          \frac{dt}{dv}=\frac{1-pv}{(1+v)^{p+2}}.
 \tag{30}
\]
This defines the analytic inverse \(v(t)\) near zero.
For \(G=U/((p+1)-pU)=(1+v)/(1-pv)\),
\[
                              G\,dt=(1+v)^{-p-1}\,dv.
 \tag{31}
\]
Taking a small-circle coefficient residue and changing the analytic
coordinate from \(t\) to \(v\) yields
\[
 [t^n]G(t)
  =\operatorname{Res}_{v=0}
                 \frac{(1+v)^{(p+1)n}}{v^{n+1}}\,dv
  =\binom{(p+1)n}{n}.
 \tag{32}
\]
This proves the algebraic formula in (11) directly.

The inverse branch starting at zero reaches
\[
 v_*=\frac1p,\qquad U_*=\frac{p+1}p,\qquad
                         t_*=\frac{p^p}{(p+1)^{p+1}}.
 \tag{33}
\]
For instance \(t(v)\) is strictly increasing on the real interval
\(0\le v<1/p\), so this is a continuation of the specified germ.
At that point \(t'=0\), while
\[
                   t''(v_*)=-p(1+v_*)^{-p-2}\ne0.
 \tag{34}
\]
The function \(G=(1+v)/(1-pv)\) has a simple nonzero pole in
\(v-v_*\). Equations (33)--(34) thus give a nonzero inverse-square-root
singularity in \(t-t_*\).
Under \(t=\kappa\eta^p/(p+1)\), each preimage is nonzero and has
nonzero derivative. This proves (12), with nontrivial local
square-root monodromy at each point. The paths obtained by lifting
\(0<t<t_*\) identify these singularities with the original germ.

The singular factor is nonzero because \(r\ne0\). More explicitly,
on the branch just described its leading form is
\[
 G(t)=\sqrt{\frac{p+1}{2p}}\,
                    (1-t/t_*)^{-1/2}+O(1).
 \tag{35}
\]
This follows by the quadratic Taylor expansion in (30); the other
continued square-root sign gives the corresponding opposite term.
Nonvanishing, rather than a global description of every algebraic
sheet, is the assertion needed here.

## 6. Calibration with the actual classical branches

Factor out the abelian root from the displayed classical symbol,
only for this classical calculation:
\[
 P(\alpha+z,1+v)=v\,Q(z,v),\qquad
 Q(z,v)=p_1z+q_0v^p+O(z^2,zv,v^{p+1}),
 \tag{36}
\]
where \(p_1=P_{YL}(\alpha,1)\) and
\(q_0=\partial_L^{p+1}P(\alpha,1)/(p+1)!\).
Both are nonzero. With \(z=s^p\), put \(v=s\lambda\).
Then \(s^{-p}Q(s^p,s\lambda)\) is holomorphic and equals
\(p_1+q_0\lambda^p\) at \(s=0\).
Its \(p\) roots are simple. The ordinary analytic implicit function
theorem therefore gives the \(p\) partner branches
\[
 \ell_j(s)=1+s\lambda_j+O(s^2),\qquad
                         \lambda_j^p=-p_1/q_0 .
 \tag{37}
\]
This proves the ramified branch statement without a formal
quantum-factor replacement.

Define their relative actions on the same ramified chart by
\[
 S_j(0)=0,\qquad dS_j=\log\ell_j\,d\log Y .
 \tag{38}
\]
Since \(Y=\alpha+s^p\),
\[
 S_j(s)=\sigma_j s^{p+1}+O(s^{p+2}),\qquad
                         \sigma_j=\frac{p\lambda_j}{\alpha(p+1)}.
 \tag{39}
\]
Finally, (6) gives
\[
 \kappa=(-1)^{p+1}\alpha^p q_0/p_1,\qquad
                    (-\sigma_j)^p
                       =\frac{p^p}{(p+1)^p\kappa}.
 \tag{40}
\]
Thus the exceptional singularities are exactly the leading scaled
negative actions \(-S_j(s)/s^{p+1}\), with the correct signs.
This matches their leading scale; it does not locate a full moving
Borel singularity for \(s\ne0\).

If the supplied source operator annihilates
\((Y-1)\mathscr W\), use its actual composition with multiplication
by \(Y-1\) in (4), as in [G]. At \(\alpha\ne1\), this multiplies
the relevant classical derivatives \(B,C\) by the same nonzero
unit. The ratio \(\kappa\), collision order and profile therefore
remain unchanged. No peripheral factor is discarded.

## 7. Complete proof sources and scope

| Label | Complete proof direct | SHA256 |
|---|---|---|
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |
| G | notes/research_classical_verma_borel_pole_profile.md | 6ba957d7a521524f370cb3bdd90ab30338bff8c13960ae6ca1825d08260c77d2 |

F supplies the original cut source, actual finite-color compatibility,
rational-loop meromorphicity and residue. G supplies the \(h=\log Q\)
coordinate and its unconditional compact-meridian Gevrey estimate,
proved from the literal finite-sector source. Its optional \(p=1\)
node theorem is not a premise for this higher-collision argument.
All improved pole estimates, exact higher residues, ramified
convergence, algebraic profile and action calibration are proved above.

For \(p=1\), the result recovers the previous square-root exceptional
profile. For \(p>1\), it gives a jointly holomorphic initial ramified
germ and the explicit one-variable exceptional restriction. It does
not give joint continuation to those singular points for nonzero \(s\),
a regular moving minor, a cutoff connection formula, or a physical
source coefficient. The hypotheses in (5) remain conditions on an
actual annihilator, and a simple Alexander root alone does not assert
them. No claim about geometric character components, arbitrary short
fillings, or a scalar lower bound is made.

Only written mathematics and complete source-text reads were used.
No mathematical programs, tests or builds were run. Frozen notes
and public manuscripts are unchanged.
