# Actual abelian transport and an operator-symbol collision test

Private written proof, 17 November 2026.

The original classical Verma source forces a specific first-order
transport identity for every actual normal-state annihilator.
It forces all Alexander roots into the zero set of the derivative
of the classical symbol along its abelian branch. Two additional
derivative tests then identify a transverse second shift branch
and determine the subprincipal value at that node.

The second branch is a branch of the actual operator's classical
symbol. No identification with an irreducible character component,
the geometric component, an analytic quantum solution, or the
selected root-of-unity cycle is asserted.

## 1. Original source and coefficient ordering

Use the original reduced, zero-framed completion proved in [F].
In the coordinate \(h=\log Q=2\log q\), put
\[
 \mathcal C(h,Y)=\mathcal W_K(1-e^h,Y),\qquad
 v(h,Y)=(Y-1)\mathcal C(h,Y).
                                                               \tag{1}
\]
These are formal series with rational meridian coefficients.
The actual leading normal state is
\[
                   v_0(Y)=\frac{Y-1}{\Delta_K(Y)},
 \qquad \Delta_K(1)=1.                             \tag{2}
\]
In particular no unknown abelian scalar multiplies (2).

Let a supplied actual normal-state annihilator, after its recorded
denominator clearing and normalization, be
\[
 B(h,Y,T)=\sum_{i\in I}b_i(h,Y)T^i,\qquad
 T f(Y)=f(e^hY),                                   \tag{3}
\]
where \(I\) is a fixed finite set of integers. Its coefficients
are regular at \(h=0\) and Laurent polynomial in \(Y\).
More locally, holomorphic coefficients near every point under
discussion suffice. A rational monic representative with poles
at an Alexander root does not satisfy this local regularity
condition until its denominators have been retained and cleared.

Write
\[
 b_i(h,Y)=b_{i,0}(Y)+h b_{i,1}(Y)+O(h^2),\quad
 P(Y,\Lambda)=\sum_i b_{i,0}(Y)\Lambda^i,\quad
 P_1(Y,\Lambda)=\sum_i b_{i,1}(Y)\Lambda^i .
                                                               \tag{4}
\]
Assume \(P\ne0\), as for a primitive representative after removal
of its common \(q-1\) valuation. All formulas below use this
left coefficient ordering and \(h=\log Q\).
The actual compatibility in [F, Section 5] gives \(Bv=0\).
It also proves
\[
                              P(Y,1)=0.                        \tag{5}
\]
Thus \(P=(\Lambda-1)U\) in the Laurent symbol ring.

## 2. The forced transport identity

Set \(E=Y\partial_Y\) and \(p(Y)=P_\Lambda(Y,1)\).
Since \(T^i=e^{ihE}=1+ihE+O(h^2)\), the coefficient of \(h\)
in \(Bv=0\), using (5), is exactly
\[
                  Yp(Y)v_0'(Y)+P_1(Y,1)v_0(Y)=0.
                                                               \tag{6}
\]
There is no unknown \(v_1\) in this equation: its coefficient
is \(P(Y,1)\), which vanishes identically.

Substitution of (2) yields the polynomial identity
\[
 Yp(Y)\bigl[\Delta_K(Y)-(Y-1)\Delta_K'(Y)\bigr]
       +P_1(Y,1)(Y-1)\Delta_K(Y)=0.                \tag{7}
\]
Equivalently, as an identity of rational functions,
\[
 P_1(Y,1)
   =Yp(Y)\left(\frac{\Delta_K'(Y)}{\Delta_K(Y)}
                                      -\frac1{Y-1}\right).
                                                               \tag{8}
\]
This fixes the subprincipal restriction from the actual abelian
source, rather than choosing a subprincipal ordering to fit a model.

Let \(\operatorname{rad}\Delta_K\) mean a square-free product of
its distinct nonzero roots, defined up to a Laurent unit.
Equation (8) proves
\[
                 (Y-1)\operatorname{rad}\Delta_K(Y)
                                      \ \bigm|\ p(Y).           \tag{9}
\]
Indeed \(\Delta_K'/\Delta_K\) has a simple pole with nonzero
integral residue at every zero of \(\Delta_K\), while the other
term in parentheses is regular there. Since \(Y\ne0\) and
\(P_1\) is regular, \(p\) must vanish at every such root.
At \(Y=1\), the first term is regular and the second has a simple
pole. Hence \(p(1)=0\) as well. These factors are relatively
prime because \(\Delta_K(1)=1\). If \(p\equiv0\), (9) is
understood in the usual divisibility sense and (8) gives
\(P_1(Y,1)\equiv0\).

There is also a precise value at each forced collision.
If \(\alpha\ne0\) is a root of multiplicity \(m\ge1\), write
\(\Delta_K(Y)=(Y-\alpha)^m d(Y)\), \(d(\alpha)\ne0\).
Then \(\alpha\ne1\) and (8), with \(p(\alpha)=0\), gives
\[
                 P_1(\alpha,1)
                       =m\alpha P_{Y\Lambda}(\alpha,1).
                                                               \tag{10}
\]
This remains true when \(p\) vanishes to higher order:
both sides then vanish. At the retained normal zero one instead has
\[
                         P_1(1,1)=-P_{Y\Lambda}(1,1).
                                                               \tag{11}
\]
The sign difference comes from the numerator \(Y-1\) in (2).

## 3. What is forced, and a checkable transverse-branch test

If the abelian factor has generic multiplicity one, then
\[
              U(Y,1)=p(Y)\not\equiv0.
                                                               \tag{12}
\]
Consequently every Alexander root satisfies \(U(\alpha,1)=0\).
This conclusion alone does not provide a second nonvertical
shift branch. A vertical factor of \(U\), vanishing at \(Y=\alpha\),
can account for it. Primitive quantum coefficients do not exclude
a common meridian factor of their classical specialization.
Nor does (9) identify any operator component with a character
component.

The following tests avoid this ambiguity. Suppose
\[
             P_{\Lambda\Lambda}(\alpha,1)\ne0,
             \qquad P_{Y\Lambda}(\alpha,1)\ne0.     \tag{13}
\]
Both are direct algebraic tests on the specified actual symbol.
They imply (12) locally and
\[
 U_\Lambda(\alpha,1)=\tfrac12P_{\Lambda\Lambda}(\alpha,1)\ne0,
 \qquad
 U_Y(\alpha,1)=P_{Y\Lambda}(\alpha,1)\ne0.
                                                               \tag{14}
\]
The holomorphic implicit-function theorem now gives a unique
second branch \(\Lambda=\ell(Y)\) through the point, with
\[
 \ell(\alpha)=1,\qquad
 \ell'(\alpha)
       =-\frac{2P_{Y\Lambda}(\alpha,1)}
                        {P_{\Lambda\Lambda}(\alpha,1)}\ne0.
                                                               \tag{15}
\]
Locally, with \(H\) a nonvanishing holomorphic function,
\[
 P(Y,\Lambda)=
       H(Y,\Lambda)(\Lambda-1)(\Lambda-\ell(Y)),\qquad
 H(\alpha,1)=\tfrac12P_{\Lambda\Lambda}(\alpha,1).
                                                               \tag{16}
\]
The factorization of \(U\) follows, for example, by integrating
its \(\Lambda\) derivative between \(\ell(Y)\) and \(\Lambda\).
The two branches are transverse. Equivalently, (5) makes
\(P_{YY}(\alpha,1)=0\), and their Hessian discriminant is
\(P_{Y\Lambda}(\alpha,1)^2\ne0\).

If only the first condition in (13) holds, a smooth second
shift branch still exists but can be tangent to the abelian
branch. If it fails, no smooth second branch is claimed here.
These alternatives are not discarded by a geometric interpretation.

## 4. The subprincipal constant in the node scaling

The effect on the formal local operator is explicit. Under (13)
set \(h=\varepsilon^2\), \(Y=\alpha+\varepsilon s\), and define
\[
 A=\frac{\alpha^2}{2}P_{\Lambda\Lambda}(\alpha,1),\qquad
 B_*=\alpha P_{Y\Lambda}(\alpha,1),\qquad
 D=P_1(\alpha,1).
                                                               \tag{17}
\]
Here \(A B_*\ne0\). The leading operator after division by
\(\varepsilon^2\) is
\[
                  A\partial_s^2+B_*s\partial_s+D.
                                                               \tag{18}
\]
To verify it in the stated ordering, substitute
\(T=\exp[\varepsilon(\alpha+\varepsilon s)\partial_s]\)
in (3). The constant and linear terms vanish by
\(P=P_Y=P_\Lambda=0\) at the point. At quadratic order the
second derivative coefficient is
\(\alpha^2\sum_i i^2b_{i,0}/2
 =\alpha^2P_{\Lambda\Lambda}/2\);
the mixed term is \(\alpha sP_{Y\Lambda}\partial_s\).
The \(s^2\) multiplication term vanishes because
\(P_{YY}(Y,1)=0\), and the remaining scalar is \(P_1\).
This proves (18) directly from the actual operator coefficients.

Equation (10) forces
\[
                              D=mB_* .                         \tag{19}
\]
For a simple Alexander root this specializes to
\[
 A\partial_s^2+B_*s\partial_s+B_*
                       =\partial_s(A\partial_s+B_*s).
                                                               \tag{20}
\]
The original normal source has nonzero residue
\[
                       r=\frac{\alpha-1}{\Delta_K'(\alpha)}.
                                                               \tag{21}
\]
Thus a formal inner solution with its prescribed algebraic tail
\(y(s)\sim r/s\) has
\(A y'(s)+B_*s y(s)=B_*r\ne0\).
This identifies the forced constant of the leading node equation.
It does not assert the existence of such a scaling limit of the
actual analytic finite source, or determine its homogeneous
Gaussian integration constant.

## 5. Gauge scope and the remaining distinction

Multiplying (3) by a scalar unit regular and nonzero at
\((h,Y)=(0,\alpha)\) multiplies \(A,B_*,D\) by its same
nonzero value, so (19) and tests (13) are unchanged.
Multiplying by a scalar with a zero or pole there is different:
it may create a vertical classical factor or a singular
coefficient representative. Such a factor must be retained.

More generally change the state by a holomorphic unit
\(\widetilde v=g(h,Y)v\) and transport the operator as
\(\widetilde B=gBg^{-1}\).
The principal symbol is unchanged, while direct expansion gives
\[
 \widetilde P_1(Y,\Lambda)
       =P_1(Y,\Lambda)
          -(Y\partial_Y\log g(0,Y))\,\Lambda P_\Lambda(Y,\Lambda).
                                                               \tag{22}
\]
Because \(P_\Lambda(\alpha,1)=0\), the value \(D\) at the
collision is unchanged. The residue in (21) is multiplied
by \(g(0,\alpha)\), which is nonzero. The reduced and normal
source gauges differ by \(Y-1\), a unit at every Alexander
root, so they give the same collision constant \(D\).
At \(Y=1\) that gauge is not a unit, as (11) records.

All assertions use the original zero-framed source.
The analytic splitting and derivatives in (13)--(16) belong to
its actual operator symbol, not an assumed AJ polynomial.
They neither prove (13) for every knot operator nor identify
the second branch as geometric. Even where (13) holds, the
node scaling above is formal. No uniform quantum-to-node
connection, Borel summation, global cycle transport, or
nonzero selected geometric coefficient follows.

The only complete proof direct is:

| Label | Complete source | SHA256 |
|---|---|---|
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |

F supplies the actual canonical completion, its normalization
and compatibility with the original normal-state operator.
Every transport, divisibility, local factorization and gauge
calculation used here is written above. The complete direct
and final text were read in full and their used implications
checked. No mathematical programs, tests, numerical cases
or builds were used. Frozen files remain unchanged.
