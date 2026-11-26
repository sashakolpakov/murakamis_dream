# Noncyclotomic Alexander roots have finite soft order

Private written proof, 18 November 2026.

The attached critical curve of the original highest-cut source cannot
be vertical at a simple Alexander root which is not a root of unity.
The proof retains the preferred longitude and uses an elementary
boundary-symbol and valuation calculation on the corresponding
classical representation curve. A classical change of frame in that
calculation makes no change to the quantum cut or its source.

This gives an algebraic criterion for the finite-order alternative
in [C]. It does not identify the attached component as hyperbolic,
prove its coefficient in a physical period, or cover knots with
Alexander polynomial one.

## 1. Statement and actual source data

Let \(K\) be a knot, represented by the fixed finite braid used for
its original one-component highest-cut source. Let
\(\alpha\ne0,1\) be a simple zero of its Alexander polynomial.
Use the actual local source of [C] and [S]:
\[
 z=Y-\alpha,\qquad
 f(Y,x)=zx-\Psi(Y,x),\qquad \Psi(Y,x)=O(x^2).
 \tag{1}
\]
Here \(x\) is the soft invariant, not a meridian eigenvalue.
The original projector is \(T_0=\operatorname{diag}(0,1,\ldots,1)\).
The stationary quotient is exactly
\[
 \mathbb C\{z,x\}/\bigl(x f_x(Y,x)\bigr).
 \tag{2}
\]
Its attached component is the smooth graph \(z=\zeta(x)\)
defined by \(f_x=0\). For \(x\ne0\) it parametrizes irreducible
characters, with a separating character coordinate
\(x+O(zx,x^2)\). These are the full local converse and quotient
statements of [C], including their zero-coordinate faces.

Choose \(x_0^2=Y\) holomorphically. The retained cut meridian is
\[
 \mu_1=\operatorname{diag}(M,M^{-1}),\qquad M=-x_0,
 \tag{3}
\]
with highest eigenline \(\mathbb C(1,0)\). Write \(L\) for the
preferred longitude eigenvalue on that line.

**Theorem.** If \(\zeta\equiv0\), then \(\alpha\) is a root
of unity. Consequently, if \(\alpha\) is not a root of unity,
there are a finite integer \(p\ge1\) and \(\tau\ne0\) such that
\[
 \Psi(\alpha,x)=\tau x^{p+1}+O(x^{p+2}),\qquad
 \zeta(x)=(p+1)\tau x^p+O(x^{p+1}).
 \tag{4}
\]
In particular the finite-ramification conclusions of [C] apply;
for sufficiently small nonzero \(z\), the resulting critical
points are folds.

We prove more explicitly that on the general critical graph,
including a potentially vertical one,
\[
                  L=\exp\{-Yf_Y(Y,x)\}.
 \tag{5}
\]
If that graph is vertical, its longitude satisfies
\[
                         L=1-\alpha x+O(x^2).
 \tag{6}
\]
The nonconstant boundary image in (6) is essential to the proof.
A curve with both peripheral eigenvalues constant would not give
the valuation contradiction below.

## 2. Preferred longitude on the general critical graph

The source identity [S, (26)--(28)] uses no nonzero quadratic
soft coefficient or Morse hypothesis. It gives, on \(f_x=0\),
\[
 \mathcal R(Y,e^\Theta)=e^{-Yf_Y},\qquad
 \mathcal R(Y,X)=X^{H/2}N(Y,X)/D(Y,X).
 \tag{7}
\]
The denominator is a unit near the initial point:
\[
 D(\alpha,\mathbf1)
   =(1-\alpha^{-1})^{\ell_+}(1-\alpha)^{\ell_-}\ne0.
 \tag{8}
\]
All clocks in \(\Theta\), and \(H,N,D\), are those of the
original exact meridian row. We check the preferred labeling,
instead of inferring it from a derivative along a nonvertical
branch.

For a coherent strand with fields \((Z,P)\), put \(t=ZP\).
The regular Gauss chart of [C] is
\[
 K_{\rm str}=x_0e^{-t},\qquad f_{\rm str}=Z,\qquad
 e_{\rm str}
    =P\,\frac{(1-e^t)(1-Ye^{-t})}{x_0t}.
 \tag{9}
\]
Define the balanced eigenvector coordinate
\[
                       \pi=P\,\frac{1-e^t}{t}.
 \tag{10}
\]
Its final factor has value \(-1\) at zero. Thus (10) is
holomorphic even when either field or their product vanishes.
For
\[
 b_+=\begin{pmatrix}K_{\rm str}&e_{\rm str}\\0&1\end{pmatrix},
 \qquad
 b_-=\begin{pmatrix}1&0\\-K_{\rm str}f_{\rm str}&K_{\rm str}\end{pmatrix},
 \tag{11}
\]
direct substitution gives
\[
                    b_-^{-1}b_+(\pi,1)^T
                              =x_0^{-1}(\pi,1)^T.
 \tag{12}
\]
Indeed \(e_{\rm str}=(x_0^{-1}-K_{\rm str})\pi\) and
\(f_{\rm str}\pi=1-e^t\).

At a crossing let \(a,b,n\) be the actual input occupations and
transfer, and set \(A=e^a,B=e^b,C=e^n\). The signed overpass
units are
\[
 \tau_+=\frac{BC}{x_0}\frac{1-Y/A}{1-YC/A},
 \qquad
 \tau_-=\frac{x_0}{A}\frac{1-Y/B}{1-YC/B}.
 \tag{13}
\]
All denominators are units near the zero-field point. The
rational signed Gauss maps of [M] give, for the globally
transported vectors
\(v_j=B_{-,j-1}^{-1}(\pi_j,1)^T\), where
\(B_{-,j}=b_{-,j}\cdots b_{-,1}\),
\[
 v'_{\rm under}=-\mu_{\rm over}^{-\epsilon}v_{\rm under},
 \qquad v'_{\rm over}=\tau_\epsilon v_{\rm over}.
 \tag{14}
\]
These are also the explicit vector identities proved in
[Q, Section 3] and [L, Sections 2--3]. For example the positive
underpass uses
\(G_1^{-1}b_{-,1}^{-1}=b_{+,1}^{-1}\), whose second row is
\((0,1)\), with \(G_1=b_{-,1}^{-1}b_{+,1}\).
In the old multiplicative momentum coordinates \(\widehat p\),
put \(\mathfrak p(A)=(1-A)(1-Y/A)/x_0\).
The positive overpass is the balanced form of
\(\widehat p'_2=(BC/x_0)\mathfrak p(A)\widehat p_1/
\mathfrak p(A/C)\). Multiplying by \(1-A/C\), and using
\(\pi=(1-A)\widehat p\), leaves exactly \(\tau_+\pi_1\).
The inverse signed identity follows by the inverse Gauss map.
Both sides of (14) are holomorphic in (9)--(10); their dense
rational identities therefore extend across every zero
occupation in this local chart.

By [C], all strand fields close, including the original cut,
where both fields are zero. Its vector in (12) is \((0,1)^T\),
the \(M^{-1}\) eigenline, opposite to (3). Follow the single
knot through the word. If \(W\) is the left-ordered product
of the underpass matrices \(\mu_{\rm over}^{-\epsilon}\),
then (14) gives
\[
 1=(-1)^{c_\times}\left(\prod\tau_\epsilon\right)
                      \operatorname{eig}_{M^{-1}}(W).
 \tag{15}
\]
The oriented blackboard parallel has word \(W^{-1}\) and
linking number equal to the writhe \(w\). Thus the preferred
longitude is \(W^{-1}\mu_1^{-w}\), in the convention fixed
in [Q]. Since \(c_\times\equiv w\pmod2\) and \(M=-x_0\),
its eigenvalue on the line (3) is
\[
                          L=x_0^{-w}\prod\tau_\epsilon^{-1}.
 \tag{16}
\]
This retains the full writhe and eigenflag, including their signs.

For completeness the local factors of the actual \(\mathcal R\)
in (7), written out in [L, (21)], are
\[
 R_+=e^{(-a-b+n)/2}
          \frac{1-Y^{-1}e^{a-n}}{1-Y^{-1}e^a},\qquad
 R_-=e^{(a+b-n)/2}
          \frac{1-Ye^{n-b}}{1-Ye^{-b}}.
 \tag{17}
\]
If \(c=b+n\) or \(b-n\) is the left output occupation, direct
cancellation gives
\[
 R_+=e^{(c-a)/2}x_0^{-1}\tau_+^{-1},\qquad
 R_-=e^{(c-a)/2}x_0\tau_-^{-1}.
 \tag{18}
\]
For \(J=-\sum j\,t_j\) on a braid stage, integer matching
continued to these analytic occupations gives
\(J_{\rm out}-J_{\rm in}=c-a\). All occupations close,
so their sum is zero, without any choice of square root.
Multiplying (18) proves \(\mathcal R=L\) in (16). Equations
(7) and (16) establish (5) on the general critical graph.

If that graph is vertical, [C] gives
\(\Psi(\alpha,x)\equiv0\). The joint \(O(x^2)\) statement in
(1) gives \(f_Y(\alpha,x)=x+O(x^2)\). Equation (6) follows.

## 3. An algebraic curve carrying a vertical source germ

We justify the curve used below; an arbitrary analytic path in a
representation variety need not have one-dimensional algebraic
closure.

Assume the graph is vertical. Choose a sufficiently small
nonzero point \(x_*\) on it. Its representation is irreducible
by [C]. Fix the cut matrix (3), now with constant eigenvalues.
Diagonal conjugation is the remaining effective gauge. Some
input lower Gauss coordinate \(f_j\) is nonzero. Fix its value
to \(f_j(x_*)\) by that gauge on a neighborhood.

This is an algebraic slice: the Gauss coordinates are rational
in the representation matrices, with unit principal-minor
denominators, as explicitly reconstructed in [C, (25)--(30)].
Clear only those unit denominators and retain the open chart.
The exact local converse and quotient (2) show that, at \(x_*\),
the representation equations with this slice and \(Y=\alpha\)
have a one-dimensional smooth germ with coordinate \(x\).
Take the irreducible algebraic component containing this germ.
Its dimension is one, and \(Y=\alpha\) on that component
because this equation was imposed before taking the component.

Let \(F_0\) be its function field. The actual representation
matrices and preferred peripheral word are defined over \(F_0\).
In particular
\[
                      M=m_0,\qquad m_0^2=\alpha,
                      \qquad L\in F_0^\times
 \tag{19}
\]
with the sign in (3). Equation (6) makes \(L\) nonconstant
on this curve. We next prove directly the obstruction to (19).

## 4. The classical boundary symbol, with generic framing only

Consider any such algebraic representation curve with noncentral
meridians of distinct eigenvalues. The following argument concerns
classical matrices only.

Adjoin two independent frame parameters to \(F_0\). Let \(w_-\)
be the inverse-meridian eigenvector at the cut. Choose a covector
\(\lambda\) with \(\lambda(w_-)=1\), and a vector \(v\) with
\(\lambda(v)=1\); the basis \((v,w_--v)\) puts that flag at
projective coordinate one. These choices are rational over a
purely transcendental field \(F=F_0(s,t)\). For instance, when
\(w_-=(0,1)\), use
\(\lambda=(t,1)\), \(v=(s,1-ts)\); the basis determinant is \(s\).

The choices can be generic at every stage of the finite word.
For each partial meridian product \(P\), its upper-left entry
in this frame is \(\lambda(Pv)\). Its vanishing is not
identical on \(\lambda(v)=1\), since \(P\) is invertible.
The condition \(e_j=0\) says that \(\lambda\) is a left
eigenline of a stage meridian. The condition \(f_j=0\) says
that \(v\) is an eigenline of \(P_{j-1}^{-1}P_j\).
These are finitely many forbidden lines for noncentral
meridians; the additional principal-minor conditions exclude
finitely many points after choosing \(\lambda\).
Thus all stage \(K_j,e_j,f_j\) are nonzero over \(F\).

In the balanced coordinates of [M], this makes every crossing's
five shapes different from zero and one. At a positive crossing
they are represented by
\[
              [B]+[C]+[Y/A]-[BC]-[YC/A];
 \tag{20}
\]
at a negative crossing use
\([A]+[C]+[Y/B]-[AC]-[YC/B]\).
For example \(e_jf_j\ne0\) excludes the two forbidden input
values \(1,Y\), the corresponding output conditions exclude
them at the outputs, and the nonzero crossing product
\(e_1f_2\) or \(e_2f_1\) excludes \(C=1\).
The Gauss denominators are nonzero on the chosen chart.
The signed expression is the one in [M]; no additional minus
sign is inserted into the already inverse-crossing symbol.

Here is the boundary calculation in
\(\bigwedge^2(F^\times\otimes_{\mathbb Z}\mathbb Q)\).
For \(\delta[z]=z\wedge(1-z)\), a signed dilogarithm sum
\(\Phi=\sum\epsilon_j\operatorname{Li}_2(z_j)\) with monomial
shapes satisfies
\[
          \delta\beta=-\sum_i X_i\wedge
                              \exp(\partial_{\log X_i}\Phi).
 \tag{21}
\]
Expand each monomial to verify this: the derivative contributes
\(-\epsilon_j n_{ji}\log(1-z_j)\).
The retained Gaussian has a symmetric quadratic coefficient
matrix, so its analogous sum vanishes by antisymmetry. Its
constant signs are torsion. Consequently \(\Phi\) in (21)
may be replaced by the whole local generating expression.

The positive canonical equations are
\(e^{S_a}=p'_2/p_1,\ e^{S_b}=p'_1/p_2,\
e^{S_c}=p'_1/p'_2\).
They turn the first three terms in (21) into
\[
 A\wedge p_1+B\wedge p_2
              -(BC)\wedge p'_1-(A/C)\wedge p'_2 .
 \tag{22}
\]
For the inverse crossing \(U=B/C,V=AC\) and
\(e^{S_c}=p'_2/p'_1\), giving the same input-minus-output
formula. All shared legs cancel in the whole word.
In the present classical frame the two cut momenta are one,
so their terms vanish as well.

The remaining meridian term is
\(-x_0\wedge e^{\partial_{\log x_0}S}\).
The exact half-step and full preferred-longitude transport of
[Q] give \(e^{\partial_{\log x_0}S}=L^2\); equivalently this
is the last term in [M, (8.1)--(8.2)], with its marking fixed
by (15)--(16). The pivot's exponentiated internal multipliers
are one, and its meridian and framing constants are roots of
unity; they introduce no omitted term in this rational wedge.
Thus
\[
                         \delta\beta=-2M\wedge L,
                         \qquad M=-x_0.
 \tag{23}
\]
The central sign disappears only in the rational wedge.
This use of a classical inverse-flag frame has changed neither
the highest-cut quantum functional nor the source in (1).

## 5. Steinberg and the tame calculation

Define Milnor \(K_2^M(F)\) as the abelian group on bilinear
symbols \(\{a,b\}\), \(a,b\in F^\times\), with
\(\{a,1-a\}=0\) for \(a\ne1\). The Steinberg relations for
\(a\) and \(a^{-1}\) give
\(\{a,a\}=\{a,-1\}\), hence
\(\{a,-a\}=2\{a,-1\}=0\).
Expanding \(\{ab,-ab\}=0\) then gives antisymmetry.
The diagonal symbols are two-torsion. Therefore the rational
wedge maps naturally to \(K_2^M(F)\otimes\mathbb Q\).
Each summand \(z\wedge(1-z)\) in (23) maps to zero. It follows
that \(\{M,L\}\) is zero after tensoring with \(\mathbb Q\),
or, equivalently, is torsion in integral \(K_2^M(F)\).

We give the required valuation homomorphism explicitly.
For a discrete valuation with uniformizer \(\pi\), write
\(a=\pi^r u,\ b=\pi^s v\), with units \(u,v\), and put
\[
       \partial\{a,b\}
           =(-1)^{rs}\bar u^{\,s}/\bar v^{\,r}.
 \tag{24}
\]
It is bilinear by its displayed exponents. It kills the
Steinberg relation in all three valuation cases:

* If \(r>0\), then \(s=\operatorname{ord}(1-a)=0\) and \(\bar v=1\).
* If \(r=0\), then either \(s=0\), or \(s>0\) and \(\bar u=1\).
* If \(r<0\), then \(s=r\) and \(\bar v=-\bar u\).
  Formula (24) is then \((-1)^{r^2-r}=1\).

Thus (24) is a homomorphism from \(K_2^M(F)\) to the
multiplicative residue field.

Normalize a projective closure of the algebraic curve in Section 3.
Its nonconstant rational function \(L\) has a zero or pole there:
otherwise both \(L\) and \(1/L\) would be holomorphic on the
compact normalization, forcing constancy. Choose such a valuation,
with \(d=\operatorname{ord}(L)\ne0\), trivial on \(\mathbb C^\times\).
It extends to \(F_0(s,t)\) by the Gauss valuation, taking the
minimum valuation of polynomial coefficients and extending to
fractions. Its residue field contains \(\mathbb C(s,t)\);
in particular it preserves the nonzero constant \(m_0\).

If \(n\{M,L\}=0\), equation (24), using \(M=m_0\), gives
\[
                                m_0^{nd}=1.
 \tag{25}
\]
Thus a constant meridian on a nonconstant-longitude curve is
a root of unity. No field-transfer theorem or external
K-theory assertion is required.

## 6. Consequence and limits

For the hypothesized vertical source graph, Sections 2--3 give
precisely the algebraic curve used in Sections 4--5.
Equation (25) forces \(\alpha=m_0^2\) to be a root of unity.
This proves the theorem by contraposition.
If the graph is nonvertical, analyticity and [C] give the finite
order and ramification in (4). No uniform bound on \(p\) is
claimed.

The boundary-symbol obstruction is classical K-theory territory;
no novelty claim is made for the root-of-unity restriction itself.
Here its proof is included and applied to the actual source's
attached graph, using its nonconstant preferred longitude.
The argument does not exclude vertical branches at cyclotomic
Alexander roots, supply a seed when \(\Delta_K=1\), identify a
hyperbolic component, or estimate an original closed quantum period.

## 7. Complete written proof directs

| Label | Complete proof source | SHA256 |
|---|---|---|
| C | notes/research_general_critical_graph_representation_quotient.md | 0e617a02cd742bdc29a3e008a4e93863d1eaf6f21379cc663cded9744e28b77b |
| S | notes/research_actual_marked_minor_regular_source_cover.md | 1f10491c502dcf1781763bc410f4f139b08e899906b748b26db92262428c2ce4 |
| M | notes/marked_braid_holonomy.md | eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f |
| Q | notes/quantum_longitude_and_regulator_action.md | e8ac5dc6bab05be0dad3810311dc3a8b169ad810b898aa3db75582087dbe8aa7 |
| L | notes/research_selected_minor_preferred_longitude.md | 50448b8688d3a7b2f4245787f6ddc07eb7afecaf94391c11c0b735ea6afdbb9c |

C supplies the general critical graph, full local representation
converse and character quotient. S supplies the general critical-
divisor external identity; only Section 5 is used. M and Q supply
the literal signed Gauss and five-shape formulas and the preferred
parallel convention. L supplies their regular highest-cut vector
and local meridian-factor comparison, which Section 2 applies as
analytic identities without its former quadratic-branch premise.
The algebraic slice, rational-to-integral symbol step and all
valuation cases are proved above.

Only written mathematics, complete source reads and hash checks
were used. Frozen notes and public manuscripts are unchanged.
