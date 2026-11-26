# The actual Gauss kernel's rational collective graph

Private written proof, 18 November 2026.

The fixed-width coherent estimate K has a specific canonical graph.
After fixing total occupation and dividing the common diagonal frame,
that graph is a rational collective conjugation of the actual dressed
meridians. We identify it by its initialized coherent boundary and
the proved analytic uniqueness in K. We do not infer it by substituting
classical symbols into a high-degree matrix function.

The rational map extends farther than the estimated kernel. In
particular it has an algebraic continuation to the regular geometric
opposite-frame problem. Its generating projection, its marked
primitive, and the coefficient of an original relative cycle are
separate issues. The complete directs K, R, L are pinned below.

## 1. Literal polarizations and the classical tensor variables

Retain K's root conventions
\[
 c_0=2\pi i,\quad Q=e^{c_0/N},\quad q=Q^{1/2},\quad
 x=-q^{-1},\quad d=N-1.
 \tag{1}
\]
There are \(r\) remaining heads. On fixed degree \(T\le d\), put
\(\sigma=(T+1)/N\in I\Subset(1/2,1)\), \(C=e^{-c_0\sigma}\).
All classical formulas below use the principal value \(x=-1\).
Their total Cartan is \(K_{\rm tot}=(-1)^rC\).

Write a head's occupation as \(p\) and \(a=e^{-c_0p}\).
For a monomial output row, the actual principal symbols are
\[
 K=-a,\qquad E=w^{-1}(a-1),\qquad
 F=w(1-a^{-1}).
 \tag{2}
\]
For the ordinary-binomial input
\(c(z)=\sum_{b=0}^d\binom db z^b w_b\), the literal right action gives
\[
 \boxed{\quad
 K=-a,\qquad E=z\frac{1-p}{p}(a-1),\qquad
 F=z^{-1}\frac p{1-p}(1-a^{-1}).
 \quad} \tag{3}
\]
These are continued in their resolved charts at removable endpoints.
For example
\[
 \frac{(Ec(z))_b}{c(z)_b}
   =z\frac{d-b}{b+1}(Q^{-b-1}-1).
\]
This proves the \(E\) row in (3); the other row follows from
\((Fc)_b=(1-Q^b)c_{b-1}\).

K's weighted-row operators \(R_{Ev}\), \(R_{Fv}\) have the reciprocal
expressions. They act on the transpose leg. Exactly at this root,
\[
 E^t=-qKF,\qquad F^t=-qK^{-1}E.
 \tag{4}
\]
For example their raising coefficient is
\(Q^{-b}(1-Q^b)=Q^{-b}-1\).
Consequently K's weighted-row characteristic equations are unchanged;
extracting the underlying input tuple requires (3), not replacing
its physical input momentum by that of the transpose row.
The actual suffix Casimir is symmetric in this root basis:
for a transfer from head \(j\) to head \(i<j\), its coefficient
and the reversed coefficient are both
\[
 K_{<i}^{-1}K_{>j}
       (1-Q^{a_i+1})(Q^{-a_j}-1).
\]
In the reversed calculation the intermediate Cartans cancel and
leave \(Q^{a_i-a_j+1}Q^{-a_i-1}=Q^{-a_j}\).
The diagonal is unchanged. Thus passing from K's transposed
suffix rows to the actual input tuple (3) preserves their symbols
in precisely the order used below.

In R's factorial convention the momentum is
\[
 \pi_{\rm out}=1/w,\qquad
 \pi_{\rm in}=z(1-p)/p,\qquad
 E=(a-1)\pi,\quad F=(1-a^{-1})/\pi.
 \tag{5}
\]
These formulas fix both coherent polarizations used here.

For each physical head define
\[
 b_i^-=\begin{pmatrix}1&0\\-K_iF_i&K_i\end{pmatrix},
 \quad b_i^+=\begin{pmatrix}K_i&E_i\\0&1\end{pmatrix},
 \quad G_i=(b_i^-)^{-1}b_i^+.
\]
Put \(B_j^-=b_j^-\cdots b_1^-\) and
\[
 H_i=(B_{i-1}^-)^{-1}G_iB_{i-1}^-.
\]
Then the ordered product and its trace are
\[
 P=H_r\cdots H_1
   =\begin{pmatrix}K&E\\KF&K^{-1}+EF\end{pmatrix},
 \qquad \Omega=\operatorname{tr}P=K+K^{-1}+EF,
 \tag{6}
\]
where \(E=\sum_iE_i\prod_{j>i}K_j\) and
\(F=\sum_i(\prod_{j<i}K_j^{-1})F_i\).
The physical meridians are \(-H_i\); their flags are the same.

## 2. A rational collective map and its marked flow

On independent heads the brackets obtained from the literal root
commutators are
\[
 \{\log K_i,E_i\}=E_i,\qquad
 \{\log K_i,F_i\}=-F_i,\qquad
 \{E_i,F_i\}=K_i-K_i^{-1}.
 \tag{7}
\]
The individual \(E_iF_i+K_i+K_i^{-1}\) are Casimirs.
Let \(D_0=\operatorname{diag}(1/2,-1/2)\).
The following dressing identities hold for every based \(H_i\):
\[
 \begin{split}
 \{\log K,H_i\}&=[D_0,H_i],\\
 \{E,H_i\}&=[K e_{21},H_i],\\
 \{F,H_i\}&=[e_{12}-F D_0,H_i].
 \end{split} \tag{8}
\]
Here all unindexed variables are the full ordered totals.

For an explicit verification, start with one head and substitute
(6) in (7). The first entries in the last two rows are respectively
\(-K(H_i)_{12}\) and \((H_i)_{21}\); the remaining entries follow
from the displayed \(E,F,K\) brackets. For old based heads the
induction passes immediately through an additional independent
head, denoted by lower-case \(k,e,f\):
\[
 K_{\rm new}=Kk,\qquad E_{\rm new}=Ek+e,\qquad
 F_{\rm new}=F+K^{-1}f.
\]
For the new based head write \(B=\left(\begin{smallmatrix}
1&0\\-KF&K\end{smallmatrix}\right)\) and \(H=B^{-1}G_{\rm head}B\).
The product rule gives
\(\{X,H\}=B^{-1}(\{X,G_{\rm head}\}+[G_{\rm head},V_X])B\),
where \(V_X=\{X,B\}B^{-1}\). Direct use of (7) gives
\[
 V_{\log K_{\rm new}}=\begin{pmatrix}0&0\\KF&0\end{pmatrix},
 \quad V_{E_{\rm new}}=
 k\begin{pmatrix}0&0\\1-K^2&-E\end{pmatrix},
 \quad V_{F_{\rm new}}=
 \begin{pmatrix}0&0\\-Ff&F\end{pmatrix}.
\]
The corresponding commutator matrices for
\(\{X,G_{\rm head}\}\) are
\(D_0,\ k(ED_0+e_{21}),\ K^{-1}(e_{12}-fD_0)\).
Subtract \(V_X\) and conjugate by \(B\). The results, up to scalar
matrices, are \(D_0,\ Kk e_{21},\
e_{12}-(F+K^{-1}f)D_0\). These are exactly (8) for the new
totals. This completes the induction without a Poisson reduction
premise.

By differentiating \(\Omega=FE+K+K^{-1}\), (8) gives
\[
 \{\Omega,H_i\}=[P,H_i],\qquad
 \{\log K,\Omega\}=0.
 \tag{9}
\]
Indeed its commutator matrix is
\(FK e_{21}+E e_{12}+(K-K^{-1}-EF)D_0=P-\Omega I/2\).
Thus the trace Hamiltonian is a collective centralizer motion,
not a separate conjugation chosen independently at each head.

For a local marked primitive introduce
\[
 \Omega=z+z^{-1},\qquad u=(Kz)^{-1},\quad v=z/K.
\]
Choose consistent logarithms and dilogarithms on a simply connected
regular patch. The factorial Hamiltonian is
\[
 {\cal H}_A=c_0\Log K+
       \operatorname{Li}_2(u)+\operatorname{Li}_2(v)
       -\operatorname{Li}_2(uv)-\operatorname{Li}_2(1).
 \tag{10}
\]
It is the scalar factorial primitive of L, including the leading
\(K^d\) character. Explicitly, with
\(I(x)=[\operatorname{Li}_2(1)-\operatorname{Li}_2(e^{c_0x})]/c_0\),
the ratio has phase \(I(x+y)-I(x)-I(y)\);
multiplying by \(c_0\) and adding \(c_0\Log K\) gives (10).
Equation (10) is not asserted to be the coherent
kernel obtained by evaluating a high-degree operator at its symbol.

Its derivatives are
\[
 \begin{split}
 \partial_{\log z}{\cal H}_A
   &=\Log(1-u)-\Log(1-v),\\
 \partial_{\log K}{\cal H}_A
   &=c_0+\Log b,\qquad
 b=\frac{(1-u)(1-v)}{(1-uv)^2}
   =-\frac{EF}{K(1-K^{-2})^2}.
 \end{split} \tag{11}
\]
For the kernel convention \(v(w)A c(z)\), the canonical map is the
inverse Heisenberg flow. The actual inverse-free relation
\[
 A_N(K,\Omega)E=E A_N(QK,\Omega)
\]
follows from \(KE=QEK\). On a local nonzero scalar or amplitude
branch with Hamiltonian (10), its ratio fixes
\(E_{\rm out}=\exp(-\partial_{\log K}{\cal H}_A)E_{\rm in}\).
No global inverse of \(A_N\) is used: L's upper primary root
channels are zero.

By (9), the centralizer part of that flow is
\(\exp[-(\partial_\Omega{\cal H}_A)P]\). Its eigenvalue ratio is
\[
 \exp[-(z-z^{-1})\partial_\Omega{\cal H}_A]
                      =\frac{1-v}{1-u}.
\]
It is therefore projectively \(I-P/K\). The commuting Cartan
part is \(\operatorname{diag}(b^{-1},1)\). Dividing their product
by \(1-K^{-2}\) gives the entirely rational representative
\[
 \boxed{\quad
 g_A=\begin{pmatrix}
 0&d_0/F\\
 -F/d_0&1-EF/(K d_0)
 \end{pmatrix},\qquad d_0=1-K^{-2},\qquad \det g_A=1.
 \quad} \tag{12}
\]
In particular the map is \(H_i\mapsto g_AH_ig_A^{-1}\), and
\[
 \boxed{\quad
 K'=K,\qquad E'=-K d_0^2/F,\qquad
 F'=-EF^2/(K d_0^2),\qquad \Omega'=\Omega.
 \quad} \tag{13}
\]
Every prefix or suffix trace is preserved. Formula (12) extends to
\(F(K^2-1)\ne0\), even at \(E=0\) or \(\Omega=\pm2\).
It maps this chart birationally to \(E'\ne0,\ K^2\ne1\).
It is canonical on its regular logarithmic domain by (8)--(11);
the identity of the rational symplectic forms extends wherever
both rational charts are defined. Recovering individual head Gauss
coordinates additionally requires their relevant prefix pivots.

At fixed \(K\), the diagonal factor in (11) is the common frame
being quotiented. The projective map is already represented by
\(I-P/K\) on the smaller \(EF\ne0\) chart. A function of \(K\)
added to (10) changes the unquotiented common-moment seam and
does not change this projective graph.

## 3. Matching the actual initialized coherent boundary

We now identify (12) with K's estimated graph; the preceding
Hamiltonian calculation alone would not identify an actual branch.

Use K's ordinary-binomial boundary saddle, at output
\(\rho_1=\cdots=\rho_{r-1}=0\). To avoid confusing it with (11),
call the binomial saddle \(U\). Put
\[
 p_i=\frac{U\xi_i}{t+U\xi_i},\quad
 P_s=\sum_{i<r}p_i=t\phi'(t;C),\quad
 p_r=\sigma-P_s,\quad U=\frac{p_r}{1-p_r}.
\]
Set
\[
 A_i=e^{-c_0p_i},\quad R=A_r=\frac{CY}{1-t},\quad
 C Y^2-(1+C-t)Y+1-Ct=0,\quad Y(0)=1.
 \tag{14}
\]
These are the actual selected functions proved in K's complete
initialized boundary, not a new spectral interpolation.
Let \(\varepsilon=(-1)^r\), \(a=z_r/U\), and
\(P_0=-\varepsilon t a\). Then (3) gives, for \(i<r\),
\[
 \pi_i=(-1)^{r-i}ta,\qquad \pi_r=a .
 \tag{15}
\]

Write \(B_i=\prod_{k\le i}A_k\), \(B_0=1\).
The first \(r-1\) dressed input meridians are exactly
\[
 H_i=-I+(B_i-B_{i-1}){\cal N}(P_0),\qquad
 {\cal N}(p)=\begin{pmatrix}-1&p\\-p^{-1}&1\end{pmatrix}.
 \tag{16}
\]
For verification the partial lowering sum before head \(i\) is
\[
 F_{<i}=\frac{(-1)^{r-1}}{ta}(1-B_{i-1}^{-1}).
\]
Consequently \((B_{i-1}^-)^{-1}[\pi_i:1]\)
is \([P_0:1]\), and the upper-right entry of the conjugated
nilpotent is \(P_0B_{i-1}\). This proves (16), including its signs.

The full totals of this boundary tuple are
\[
 \begin{split}
 K&=\varepsilon C,\\
 E&=a[(1-t)R+tC-1]=a[CY+tC-1],\\
 F&=-\frac{\varepsilon}{aCt}
                  [C-t-(1-t)R]
       =-\frac{\varepsilon}{aCt}[C-t-CY].
 \end{split} \tag{17}
\]
Their trace is \(\Omega=\varepsilon\lambda_G(t)\), where
\[
                   \lambda_G(t)=C(1+Y)+t .
 \tag{18}
\]
Substitution of (14) checks this last equality directly.

The condition \((I-P/K)[P_0,1]^t\in\mathbb C e_1\) is
\[
 (1-CY)(C-t-CY)=(C^2-1)t.
\]
After division by \(C\), it is precisely the quadratic (14).
Thus the actual branch \(Y(0)=1\), rather than the other root,
is mapped by (12) to the output vacuum flags.

It is useful to verify the covectors as well. If \(g_A[P_0,1]^t\)
lies on \(e_1\), direct rank-one conjugation gives
\[
 g_A{\cal N}(P_0)g_A^{-1}
             =\frac{d_0^2}{P_0F^2}e_{12}.
 \tag{19}
\]
At output vacuum the first \(r-1\) head Cartans are \(-1\),
their lowerings vanish, and
\[
 F'=(-1)^{r-1}w_r(1-C^{-1}).
\]
Using (13) recovers its \(w_r\) in the same representative.
Let
\[
 D_*=-\frac{(1-t)^2R(R-1)}{t c_0(C-1)C}.
\]
Equations (14),(17) imply
\[
 \frac{d_0^2 w_r}{P_0F^2}
                    =-c_0(-1)^{r-1}D_*.
 \tag{20}
\]
For example the only quadratic simplification needed is
\(CY+tC-1=Y(CY-1+t)\), which is (14).

In the monomial output polarization (2), a based head at this
axis has upper-right entry
\(-c_0(-1)^{r-1}S_{\rho_i}/w_r\).
Equations (16),(19),(20) therefore give exactly
\[
        S_{\rho_i}(0,\xi)=D_*(B_i-B_{i-1}),
 \tag{21}
\]
the initialized gradients K proves from the actual finite matrix.
The input gradients are the same \(p_i\) as its boundary saddle.
This matches both sides of the initialized canonical relation.

For completeness this initial comparison determines a local graph,
not merely a set of special points. The preimage of the output
vacuum Lagrangian under the canonical map (12) is smooth. Equations
(14)--(16) parametrize it on the chosen small branch. Its map to the
input \(\xi_i\) is locally invertible: K proves
\[
 \xi_i=k(P_s)\frac{p_i}{1-p_i},\qquad
 k(P_s)=\frac{P_s}{(2/c_0)\sigma/(1-\sigma)}(1+O(P_s)),
\]
with Jacobian
\(2(P_s/[(2/c_0)\sigma/(1-\sigma)])^{r-1}(1+O(P_s))\ne0\).
Thus the graph has an analytic mixed generating function near the
axis. Set its boundary constant equal to K's actual \(\psi(\xi)\).

Collective conjugation preserves all the suffix traces in K's
principal reverse equations. Its generating function therefore
satisfies those same principal rows. K's convergent coefficient
recursion, with its nonzero low diagonal and prescribed boundary,
proves analytic uniqueness. Hence this generating function is
K's actual \(S\) on a sufficiently small connected subchart.
Analytic identity extends the equality over the connected portion
of that estimated chart on which these generating coordinates are
regular.

**Conclusion.** The canonical graph of the genuine nonzero-amplitude
kernel in K, after the fixed-degree common-frame quotient, is (12).
Its phase and coefficient are still K's initialized ones. This proof
does not extend that coefficient estimate by rational continuation.

## 4. The geometric opposite-frame criterion

Here is an explicit target for comparison with the original source.
R's complete \(F_\Sigma=0\) section has first meridian and full product
\[
 H_1^0=\begin{pmatrix}-1&0\\-F&-1\end{pmatrix},\qquad
 P_{\rm full}=\begin{pmatrix}-K&E\\0&-K^{-1}\end{pmatrix}.
 \tag{22}
\]
The selected first-meridian flag is \(e_2\); the selected total flag
is \(e_1\). If \(K^2\ne1\), the other total eigenline is
\([E/(K-K^{-1}):1]\). It differs from the meridian flag exactly
when \(E\ne0\).

Keeping that meridian flag, the change to the opposite total
eigenflag induces on the remaining tuple the common conjugation
\[
 \boxed{\qquad
 \ell=\begin{pmatrix}1&0\\(K-K^{-1})/E&1\end{pmatrix},
 \qquad (K,E,F)\longmapsto(K^{-1},E,F).
 \qquad} \tag{23}
\]
To verify the actual framing, R gives
\(H_{i+1}^{\rm full}=h_0H_i h_0^{-1}\), with
\(h_0=\left(\begin{smallmatrix}1&0\\F&-1\end{smallmatrix}\right)\).
The full-frame change is
\(\left(\begin{smallmatrix}1&0\\-(K-K^{-1})/E&1\end{smallmatrix}\right)\).
Conjugating it by \(h_0=h_0^{-1}\) gives (23).
Direct multiplication verifies the new total entries.

For complete discrete faithful holonomy with regular total product,
R proves that this product is loxodromic and that neither of its
eigenlines can equal a nontrivial parabolic meridian flag. Hence
\(E\ne0\); also \(F\ne0\), since \(H_1^0\) is noncentral.
Thus both (12) and (23) have algebraically regular representatives
at the relevant geometric frame. The unit conditions persist in a
sufficiently small holonomy neighborhood. This last observation is
not a quantum meridian-normal estimate.

These are different maps: \(A_N\) preserves the tail \(K\), whereas
the opposite kernel reverses it. The original routing is exactly
\[
 T=\mathcal B_m(W_\tau^{-1})\,A_N\,D_{\rm top}\,\mathscr C_r,
 \qquad J_{\rm op}=D_N(MK)^{-1}T .
 \tag{24}
\]
All factors, order, scalars, source pivots and meridian currents in
L remain. Comparing with (23) requires applying the turnover,
degree factor and routed reduced braid in (24), with the same cut
and presentation. One cannot identify the bare map (12) with (23),
or delete these interfaces because both preserve ordered characters.

## 5. Marks and the distinct analytic continuation gate

On regular patches (10),(11) give the collective flow time
\[
 \partial_\Omega{\cal H}_A
   =\frac{\Log(1-u)-\Log(1-v)}{z-z^{-1}}.
 \tag{25}
\]
The rational graph removes the displayed spectral square root.
It does not remove the logarithms from the action. The actual
coherent phase is obtained with the boundary calibration in Section 3;
it is not simply (10) evaluated on an input point. At fixed degree,
a remaining function of \(K\) is the common diagonal seam. A full
occupation stationary equation must still impose its closing value.

L gives a concrete finite warning against discarding marks. If the
factorial logarithms \(u=e^{c_0x},v=e^{c_0y}\) are both shifted by one,
the actual left factor of the sewn source is multiplied by
\[
 d_{{\rm deck},N}(M)=
 \frac{1-M^{-2mN}}{1-M^{-2N}}.
 \tag{26}
\]
It has value \(m\), not one, at \(M=1\), and
\(\left.\partial_\mu d_{{\rm deck},N}(e^\mu)\right|_0=-Nm(m-1)\).
Individual ordered decks can have the
actual radical poles recorded in L. Thus a rational equality of
graphs cannot reset the marked factorial lift or its normal source.

There are explicit independent tests for geometric reach.

* K's estimate has physical real \(\sigma\), so \(|K|=1\).
  The regular complete geometric total eigenvalue is loxodromic.
  Its nonreal occupation moment is outside this estimated slice.
* Given a chosen logarithmic tuple, recover
  \(p_i=-\Log(-K_i)/c_0\), the actual input
  \(z_i=\pi_i p_i/(1-p_i)\), and output \(w_i=1/\pi_i'\).
  Then test K's actual
  \(\xi_i=(-1)^{r-i}z_i/z_r\) and
  \(\rho_i=(-1)^{r-i}w_i/w_r\), including its punctured sector,
  bounded shapes, and small output domain.
  These ratios are unchanged by residual common diagonal framing.
  That freedom cannot force membership in the estimated chart.
* Even the initialized scalar projection has a genuine branch gate:
  \[
   t=\frac{(\lambda-2C)(\lambda-C-1)}
                {\lambda-1-2C+C^2},\qquad
   \Delta_B(t)=(1+C-t)^2-4C(1-Ct).
   \tag{27}
  \]
  The selected branch begins at \(\lambda=2C,t=0,Y=1\).
  The other zero-activity branch is \(\lambda=C+1\).
  The projection can ramify at \(\Delta_B=0\) while (12) remains
  regular. Higher-dimensional generating projections have their
  corresponding mixed-Hessian gates.

Equation (27) follows by eliminating \(Y\) from (14),(18).
It is a test of this initialized projection, not a global
parametrization of every tuple by its trace alone.

Consequently a geometric point can belong to the algebraic
continuation of this source graph without belonging to the domain
where K selected and estimated its coefficient. The remaining
analytic problem is transport of the original capped coherent
and occupation contour, with its complementary chains and marked
degree connectors, to the appropriate generating chart. A path
avoiding the rational poles or a unique algebraic critical point
does not supply that transport or its relative coefficient.
No meridian-normal, volume, or closed-source noncancellation
claim is made here.

## Complete proof-source pins and coverage

* K: notes/research_fixed_width_gauss_coherent_sector_kernel.md,
  SHA256 725f11b37640abd36b89ae0f1f6f47464ed6b588ccc8b7709d32e62a502045ec.
* R: notes/research_actual_reduced_braid_critical_scheme.md,
  SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.
* L: notes/research_marked_gauss_functional_calculus.md,
  SHA256 7f8c7c0be05331e7c0679c5a26374bbcb4b38b817c36a1f4ac4e16d4c1739095.

The entire final was freshly read nontruncated. Both complete R and
L were freshly reread in covering chunks here; the complete K read
from the immediately preceding matching formal review is retained
fresh and unchanged. Every used implication was checked and all
four matching hashes were renewed at the author freeze.
The earlier opposite-polarization, source-frame and finite-separator
coverage already supplies the exact routed operators, the turned
character relation and the framing warning. The new assertion here
is the explicit collective map matched to K's actual initialized
coherent graph. No general novelty claim for collective Hamiltonian
flows or changes of polarization is intended. No mathematical
programs were used. Frozen and public files were not edited.

