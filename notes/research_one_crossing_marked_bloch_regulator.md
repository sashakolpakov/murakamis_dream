# The original one-crossing critical graph and its marked Bloch regulator

22 November 2026. Written research proof. Author-final.
Earlier author-finals and public manuscripts remain unchanged.

The original four-input source with one coherent parameter zero has a
particularly simple nonconstant classical component. Its calibrated
complex primitive is symmetric in the three remaining boundary angles.
Its critical dilogarithm class is the conjugate-antisymmetric class of
three explicit positive ideal tetrahedra. This identifies a regulator of
the original source component, rather than assigning a volume to an
unrelated sum of functions.

This note does not prove that the original finite period selects this
component away from its initialized endpoint. It does not construct a
convex union of the three tetrahedra or identify a filled knot manifold.

## 1. The original finite source and its literal crossing

Use the full algebra, centered basis, and original Frobenius closing of
[B]. Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad \kappa=e^{\pi i d^2/(2N)},\qquad
 U_x=\sum_{j=0}^d x^j f_j.
 \tag{1}
\]
All powers of \(q\) have the displayed exponential convention.
The entire repeated-root algebra, including its first spectral normals,
is retained. In particular \(R^+=\sqrt N f_0\), so the source here is
exactly
\[
 \Phi_N^\times(z;s,t)
   =\phi(f_0U_zU_sU_t)
   =N^{-1/2}\phi(R^+U_zU_sU_t).
 \tag{2}
\]
The crossing and closing in (2) are the original ones. Since each unit
coherent input has norm \(\sqrt N\), normalizing the three such inputs
divides (2) by \(N^{3/2}\). No normalization changes an exponential
action in this note.

Let \(F_N(a)=\sum_{j=0}^d(-qa)^j\), \(G_N(r)=\sum_{j=0}^d r^j\), and
\((a;Q)_j=\prod_{\ell=0}^{j-1}(1-aQ^\ell)\). Specializing the exact
finite formula [B, equation (10)] at its first parameter zero gives
\[
 \Phi_N^\times(z;s,t)=\frac{\kappa^2}{N}F_N(z)G_N(st)
 \sum_{j=0}^{N-1}
 \frac{Q^j(-q/s,-q/t;Q)_j}{(-q^3z,Q/(st);Q)_j}.
 \tag{3}
\]
As in [B], the entire prefactored expression is a polynomial identity
after canceled continuation. Individual factors in (3) may vanish or
have removable poles. They are not replaced by their absolute values,
and the index is not extended beyond \(N-1\). In particular the literal
finite framing factor \(\kappa^2\) is still present.

## 2. The nonconstant critical component

Work on the contractible real angle domain
\[
 \mathcal D=\{(c,h,k):c,h,k>0,\quad c+h+k<1\},\qquad
 C=e^{-2\pi ic},\ H=e^{-2\pi ih},\ K=e^{-2\pi ik},\quad r=HK,
 \tag{4}
\]
with \(z=-C,s=-H,t=-K\). Capital \(C\) in this note is a boundary
exponential, not the centered multiplication tensor.
The exact consecutive-term ratio of the sum in (3) is
\[
 Q\frac{(1+qQ^j/s)(1+qQ^j/t)}
          {(1+q^3zQ^j)(1-Q^{j+1}/r)}.
\]
Its classical rational limit, with \(v\) denoting the internal
exponential coordinate, is
\[
 \mathcal R(v)=
 \frac{(1-v/H)(1-v/K)}{(1-Cv)(1-v/r)},\qquad
 \mathcal R(v)=1\iff
 v\{1+Cr-H-K+(1-C)v\}=0.
 \tag{5}
\]
Thus there is one nonzero critical point
\[
                  v_* =\frac{H+K-1-Cr}{1-C}.
 \tag{6}
\]
The factor \(v=0\) is not discarded as a source contribution by this
calculation. Equation (6) describes the selected nonconstant component
whose geometry we compute; period selection remains separate.

Here are all needed nondegeneracy checks on \(\mathcal D\).
The unit numbers \(C,H,K,CH,CK,HK\) differ from one. Also \(v_*\ne0\).
Indeed \(H+K=1+CHK\) would imply
\[
 \cos\pi(h-k)=e^{-\pi ic}\cos\pi(c+h+k).
\]
Its imaginary part forces \(c+h+k=1/2\), and then
\(|h-k|=1/2\), contradicting \(|h-k|<h+k<c+h+k\).
Direct substitution gives
\[
 \begin{split}
 1-Cv_*&=\frac{(1-CH)(1-CK)}{1-C},\\
 1-v_*/H&=\frac{(1-K)(1-CH)}{H(1-C)},\\
 1-v_*/K&=\frac{(1-H)(1-CK)}{K(1-C)},\\
 1-v_*/r&=\frac{(1-H)(1-K)}{r(1-C)}.
 \end{split}
 \tag{7}
\]
All four critical shape arguments \(Cv_*,v_*/r,v_*/H,v_*/K\)
therefore avoid zero and one. Their differences used below are nonzero
as well: their quotients are \(C,H,K,CH,CK\), or their inverses.
Finally, the derivative in \(v\) of the right numerator in (5) is
nonzero at \(v_*\), since it is \((1-C)v_*\). This internal critical
point remains nondegenerate even when \(h=k\).

## 3. The calibrated complex primitive and the logarithmic marks

Write \(\operatorname{Li}_2\) with its usual power-series germ. Its
continuations, and the logarithms in its derivatives, must be marked.
A local term-ratio primitive for (5), normalized to zero at \(v=1\), is
\[
 \begin{split}
 \mathcal W(v)=\frac1{2\pi i}\big[&
 \operatorname{Li}_2(Cv)+\operatorname{Li}_2(v/r)
 -\operatorname{Li}_2(v/H)-\operatorname{Li}_2(v/K)\\
 &+\operatorname{Li}_2(H^{-1})+\operatorname{Li}_2(K^{-1})
 -\operatorname{Li}_2(C)-\operatorname{Li}_2(r^{-1})\big].
 \end{split}
 \tag{8}
\]
Indeed \(2\pi i\,\partial_{\log v}\mathcal W=\log\mathcal R\).
The stationary lift has \(\log\mathcal R(v_*)=0\).

For an explicit global mark, set
\[
 \ell(a)=\log(2\sin\pi a)+i(\pi/2-\pi a),\quad 0<a<1;
 \qquad \ell(a)=\log(1-e^{-2\pi ia}).
 \tag{9}
\]
Every single angle and pair sum in (4) lies in this interval. The
marked critical differential is
\[
 \begin{split}
 \partial_c\mathcal S&=\ell(c+h)+\ell(c+k)-2\ell(c),\\
 \partial_h\mathcal S&=\ell(c+h)+\ell(h+k)-2\ell(h),\\
 \partial_k\mathcal S&=\ell(c+k)+\ell(h+k)-2\ell(k).
 \end{split}
 \tag{10}
\]
These are choices of lifted logarithms, not principal logarithms of
arbitrary quotients. Differentiating (8) at its stationary point and
using (7) proves their exponentiated identities. For example
\[
 e^{\partial_c\mathcal W_*}
 =\frac{1-Cv_*}{1-C}
 =\frac{(1-CH)(1-CK)}{(1-C)^2},\qquad
 e^{\partial_h\mathcal W_*}
 =\frac{(1-CH)(1-HK)}{(1-H)^2}.
 \tag{11}
\]
The lifted differential (10) is compatible and closed: its mixed
derivatives agree directly. It specifies the zero-winding component
of these original classical equations. This is the stated chosen
logarithmic mark, not a deduction from the exponentiated graph alone.
For example, adding \(2\pi i m h\), with an integer \(m\), preserves
that graph and vanishes at \(h=0\). The endpoint calibration below
fixes only the additive constant after (10) has been specified;
selection of this mark by the actual finite period is not proved here.
Equivalently the logarithms
in (7)--(8) are lifted so that (10) holds. The absence of zero and one
in Section 2 permits continuation of these lifts on the contractible
domain \(\mathcal D\). A different integral logarithmic lift is not
silently identified with this one.

It remains to fix the additive constant from the original source.
The exact boundary readout in [B] is
\[
 \Phi_N^\times(z;-q^{-1},t)
            =\kappa\sqrt N\,\mathcal C_N(0,z,t).
 \tag{12}
\]
Fix \(c,k\), and take \(t=-qK\) in (12). Then \(st=K\), the first
angle is \(h=1/(2N)\), and the last parameter tends to \(-K\) as
\(N\to\infty\). This initializes the boundary \(h=0\) at fixed
product. The actual zero-radius source theorem [P] has the
calibrated exponent \(i\Psi(0,-C,-K)\), where
\[
 i\Psi(0,-C,-K)
 =-\frac{i\pi}{12}
   +\frac{i}{2\pi}
       [\operatorname{Li}_2(C)+\operatorname{Li}_2(K)
                                      -\operatorname{Li}_2(CK)].
 \tag{13}
\]
Its dilogarithms are the continuous power-series limits at the displayed
unit arguments. The theorem applies here by choosing an unused radial
angle between \(1-c-k\) and \(\min(1-c,1-k)\). This interval is
nonempty. The two actual factors \(\kappa\) in (12) and in the
three-input source leave precisely \(\kappa^2\); it is not absorbed
into (13). Bounded amplitudes and polynomial normalization factors are
also not being claimed to have trivial phase.

In (8), \(h\downarrow0\) gives \(H\to1\), \(v_*\to K\), and the
calibrated limit is
\[
 \mathcal W_*\longrightarrow
 \frac{\operatorname{Li}_2(CK)-\operatorname{Li}_2(C)
                   -\operatorname{Li}_2(K)+\operatorname{Li}_2(1)}
      {2\pi i}=i\Psi(0,-C,-K).
 \tag{14}
\]
With the differential (10) already fixed, its primitive with exactly
this additive boundary constant is therefore
\[
 \boxed{\quad
 \mathcal S(c,h,k)=\frac1{2\pi i}
 \left[\sum_{\{a,b\}\subset\{c,h,k\}}
          \operatorname{Li}_2(e^{-2\pi i(a+b)})
       -2\sum_{a\in\{c,h,k\}}\operatorname{Li}_2(e^{-2\pi ia})
       +3\operatorname{Li}_2(1)\right].\quad}
 \tag{15}
\]
Thus (15) is the marked value of (8), with the differential lift just
specified. In particular the constant is **plus**
\(3\operatorname{Li}_2(1)\). The finite factors in (3) and their
aliases are not individually declared asymptotically negligible.
The statement concerns their original critical component and calibrated
primitive, not a new asymptotic theorem for the whole finite period.

Let \(L(a)=\int_0^a\log|2\sin\pi u|\,du\), extended oddly and with
period one. The unit-circle dilogarithm has
\(\operatorname{Im}\operatorname{Li}_2(e^{-2\pi ia})=2\pi L(a)\)
and real part \(\pi^2(a^2-a+1/6)\) for \(0<a<1\).
Substitution in (15) gives the exact branch identity
\[
 \mathcal S=\mathcal A_0-\pi i(ch+ck+hk),\qquad
 \mathcal A_0=L(c+h)+L(c+k)+L(h+k)-2[L(c)+L(h)+L(k)].
 \tag{16}
\]

## 4. The original boundary polynomial and its regulator orientation

Keep \(r=HK\) fixed and let \(\mathsf L\) denote the classical
multiplier for the shift \(h\mapsto h+1/N\). The original equation
[B] specializes, at its classical level, to coefficients
\[
 B_0=\frac{(1-K)^2(1-CH)}{(H-K)^2},\qquad
 D_0=\frac{(1-H)^2(1-CK)}{(H-K)^2}.
 \tag{17}
\]
Its classical right-side eigenvalue is zero. Multiplying its symbol by
\(\mathsf L\) retains both components:
\[
 (\mathsf L-1)(D_0\mathsf L-B_0)=0.
\]
After clearing its displayed denominator this is the original local
polynomial
\[
 \boxed{\quad
 A_\times=(\mathsf L-1)
 [H(1-H)^2(H-Cr)\mathsf L-(H-r)^2(1-CH)].\quad}
 \tag{18}
\]
It is an auxiliary boundary polynomial of the original source, not a
knot peripheral \(A\)-polynomial. The constant component is retained.
The nonconstant component is
\[
 \mathsf L_\times=\frac{B_0}{D_0}
 =e^{-\pi i(k-h)}
 \frac{\sin^2\pi k\,\sin\pi(c+h)}
      {\sin^2\pi h\,\sin\pi(c+k)},\qquad
 (\partial_h-\partial_k)\mathcal S=\log\mathsf L_\times.
 \tag{19}
\]
The argument on the last lift is exactly \(-\pi(k-h)\in(-\pi,\pi)\),
as follows from (9). It is not determined only modulo \(2\pi\).
The cleared components meet at \(h=k\); (17) is not applied at its
uncleared fold. Formula (15) itself is regular there.

Along fixed \(C,r\), \(d\log H=-2\pi i\,dh\). Hence
\[
 d\mathcal S=-\frac{\log\mathsf L_\times}{2\pi i}\,d\log H,
 \qquad
 \eta=\log|H|\,d\arg\mathsf L_\times
             -\log|\mathsf L_\times|\,d\arg H
           =2\pi\,d\mathcal A_0.
 \tag{20}
\]
Here the last equality is on the unit-angle locus. This checks both
the orientation and the factor of two in the regulator below.

## 5. The actual critical Bloch expression

Use the reduced pre-Bloch convention with five-term relation
\[
 [a]-[b]+[b/a]
 -\left[\frac{1-a^{-1}}{1-b^{-1}}\right]
 +\left[\frac{1-a}{1-b}\right]=0,
 \qquad [u^{-1}]=-[u],\quad[1-u]=-[u].
 \tag{21}
\]
This explicitly quotients the usual inverse/complement torsion and
real constant ambiguity. We do not claim an equality of unreduced
integral symbols or of unmarked extended dilogarithms from (21).
Their missing phase information has instead been fixed in (9)--(16).

Set \(X=v_*/H,Y=v_*/K,Z=Cv_*,W=v_*/r\), and define
\[
 \beta_\times=[Z]+[W]-[X]-[Y]
       +[H^{-1}]+[K^{-1}]-[C]-[r^{-1}].
 \tag{22}
\]
This is precisely the dilogarithm expression (8) from the original
finite term ratio, evaluated at its nonzero critical point.
Put \(A=(1-CH)/(1-H)\). Using (7), three applications of (21),
with \((a,b)=(X,W),(Z,Y),(C,H^{-1})\), give respectively
\[
 \begin{split}
 [W]-[X]&=-[K]-[A]+[KA],\\
 [Z]-[Y]&=[CK]+[A/C]-[KA],\\
 [A/C]-[A]&=[CH]-[C]-[H].
 \end{split}
 \tag{23}
\]
For example their two nontrivial arguments in the first relation are
\((1-X^{-1})/(1-W^{-1})=A\) and
\((1-X)/(1-W)=KA\). In the second they are \(A/C,KA\);
in the third they are \(1-A/C,1-A\). This verifies all substitutions
and signs without invoking a dilogarithm summation theorem.
All these arguments avoid zero and one. For instance \(A=1\) or
\(A/C=1\) would force \(C=1\); \(KA=1\) would force \(v_*=0\).
Their other denominators are nonzero by Section 2.
Adding the three identities proves
\[
 \boxed{\quad
 \beta_\times=[CH]+[CK]+[HK]-2[C]-2[H]-2[K].\quad}
 \tag{24}
\]

For a pair of distinct labels \(a,b\in\{c,h,k\}\), write
\(U=e^{-2\pi ia},V=e^{-2\pi ib}\), and put
\[
 z_{ab}=\frac{1-V}{1-UV}
       =e^{\pi ia}\frac{\sin\pi b}{\sin\pi(a+b)}.
 \tag{25}
\]
The word distinct refers to the labels; their numerical angles may
coincide. These are positive ideal-tetrahedron shapes, with angle
triples \(\pi(a,b,1-a-b)\). Indeed
\(1-z_{ab}=e^{-\pi ib}\sin\pi a/\sin\pi(a+b)\).
All three angles are strictly positive on \(\mathcal D\).
The relation (21) at \((U,UV)\), followed by
\((1-U)/(1-UV)=1-\overline{z_{ab}}\), gives
\[
 [UV]-[U]-[V]=[z_{ab}]-[\overline{z_{ab}}].
 \tag{26}
\]
Consequently (24) is exactly the conjugate-antisymmetric class of
these three positive tetrahedra.

Normalize the Bloch--Wigner function so that the oriented volume of
the ideal tetrahedron \((\infty,0,1,z)\) is
\(D(z)=\operatorname{Im}\operatorname{Li}_2(z)
          +\log|z|\arg(1-z)\).
Here is a direct check of its five-term regulator identity. The formula
for \(D\) gives
\(dD(z)=\log|z|\,d\arg(1-z)-\log|1-z|\,d\arg z\).
In (21) put \(u=b/a\), \(w=(1-a)/(1-b)\); its fourth argument is
\(uw\). Substituting
\(1-u=(a-b)/a\), \(1-w=(a-b)/(1-b)\), and
\(1-uw=(a-b)/(a(1-b))\) cancels the differential of its five terms.
The nonsingular complex parameter domain is connected, and the limit
\(b\to a\), using \(D(1)=0\), fixes the constant to zero.
The function changes sign under conjugation, and on a unit argument
\(e^{-2\pi ia}\) equals \(2\pi L(a)\). Thus (26) directly gives
\[
 D(z_{ab})=\pi[L(a+b)-L(a)-L(b)]>0,
 \qquad
 D(\beta_\times)=2\sum_{\{a,b\}}D(z_{ab})=2\pi\mathcal A_0.
 \tag{27}
\]
The strict inequality also follows directly by differentiating
\(L(a+b)-L(a)-L(b)\): it is zero at \(a=0,1-b\), and increases
then decreases, with its unique turning point at \(a=(1-b)/2\).

The same conclusion can be checked with the matching continued
dilogarithm and argument lifts in (8).
The four internal critical arguments in (22) have the same modulus
\(|v_*|\). Their correction is \(\log|v_*|\) times
\(\arg(1-Z)+\arg(1-W)-\arg(1-X)-\arg(1-Y)=0\)
on the stationary lift. The four remaining arguments are unit.
This also verifies \(D(\beta_\times)=2\pi\Re\mathcal S\) directly
from (8), consistently with (20). Replacing these continued arguments
by separate principal arguments can add an integer multiple of
\(2\pi\log|v_*|\); that operation would not compute the marked
primitive. The five-term proof of (27) avoids this branch ambiguity.

## 6. Scope and complete direct sources

We have identified an original-source local critical curve, its chosen
logarithmic component, the exact calibrated complex primitive, and its
positive three-tetrahedron regulator. The factor of two is deliberate:
\(\beta_\times\) is a conjugate-antisymmetric class, whereas the positive
three-tetrahedron chain has volume \(\pi\mathcal A_0\).

No convex-union statement, original-manifold triangulation, or primitive
knot-surgery equation is inferred from this relative class. Nor does
this computation discard another critical component or prove a nonzero
coefficient in the finite period. Such a source asymptotic requires its
own contour or recurrence proof, retaining (3), its aliases and endpoint
currents. No general short-component attachment or finite-exception
volume theorem is proved here.

| Label | Complete direct proof source | SHA-256 |
|---|---|---|
| B | [Original four-input polynomial source](research_four_coherent_boundary_polynomial_source.md) | 93241074830ff4b844ba5baafd06a15bf08ec6bddc3a1498727f110ebe297d84 |
| P | [Actual radial-zero prism source and its marking](research_single_leg_radial_turn_source.md) | c624e0edbaadb57279c00420d3f552e93c67cb84972926aad27ff51c2c973e7e |

Both complete direct sources were read at their matching pins.
Only written mathematics and text operations were used.
This research proof is author-final.
