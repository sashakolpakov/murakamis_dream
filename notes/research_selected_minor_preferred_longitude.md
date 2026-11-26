# The source-selected local action and the preferred longitude

Private written proof, 18 November 2026.

The local minor selected by the original highest-cut source has a
preferred peripheral interpretation. Its meridian derivative is
the preferred longitude eigenvalue on the retained highest eigenline.
The proof compares the exact source's peripheral expression with
eigenvector transport through the same signed braid.

This is a local A-polynomial statement. No hyperbolic-component
identification, complete regulator value, or physical quantum-cycle
coefficient is asserted.

## 1. Conventions and assertion

Use the selected actual minor and action \(S_g(Y)\) of [H], and
the local irreducible representation of [R]. These use the same
simple two-branch node, \(Y=\alpha+z\), \(\alpha\ne0,1\).
Choose \(x_0^2=Y\) holomorphically. Its retained meridian and
highest eigenline are
\[
 \mu_1=\operatorname{diag}(M,M^{-1}),\qquad
                   M=-x_0,\qquad \mathbb C(1,0).
 \tag{1}
\]
The braid writhe is \(w\). Its preferred longitude \(\lambda\)
means the oriented parallel with linking number zero.
Let \(\ell(Y)\) be its eigenvalue on the line in (1).

The original exact quantum row [E] has classical peripheral function
\[
 \mathcal R(Y,X)=X^{H/2}N(Y,X)/D(Y,X).
 \tag{2}
\]
All lattice forms and factors in \(H,N,D\) are those in [E].
The actual selected clock map is \(\Theta_g(Y)\).

**Theorem.** On a sufficiently small neighborhood of the node,
\[
 \boxed{\quad
    \ell(Y)=\mathcal R(Y,e^{\Theta_g(Y)})
                         =e^{Y S_g'(Y)} .
 \quad}
 \tag{3}
\]
The eigenline in (1), rather than its Weyl conjugate, fixes the
longitude value in (3). Both sides tend to one at \(Y=\alpha\).
With the analytic logarithm \(\log\ell(\alpha)=0\),
\[
                       dS_g=\log\ell\,d\log Y
                            =2\log\ell\,d\log M .
 \tag{4}
\]
The peripheral germ lies on a one-dimensional nonabelian
A-polynomial component:
\[
                  A_K(-\sqrt Y,e^{Y S_g'(Y)})=0,
 \tag{5}
\]
in the preferred-meridian/longitude convention. Equation (5) does
not identify that component as geometric.

## 2. A regular eigenvector at the original cut

Use [R]'s field chart, writing \((q,p)\) for one strand's
creation and momentum fields to avoid confusing them with
peripheral coordinates:
\[
 t=qp,\quad K=x_0e^{-t},\quad f=q,\quad
 e=p\,\frac{(1-e^t)(1-Ye^{-t})}{x_0t}.
 \tag{6}
\]
Define the balanced eigenvector coordinate
\[
 \pi=p\,\frac{1-e^t}{t}.
 \tag{7}
\]
This is holomorphic at \(t=0\); its factor has value \(-1\).
It also equals \((1-e^t)/q\) on the dense set where that
quotient is defined. Thus no creation field is divided out
in (7).

The triangular matrices in [R] are
\[
 b_+=\begin{pmatrix}K&e\\0&1\end{pmatrix},\qquad
 b_-=\begin{pmatrix}1&0\\-Kf&K\end{pmatrix},\qquad
 G=b_-^{-1}b_+
   =\begin{pmatrix}K&e\\Kf&K^{-1}+ef\end{pmatrix}.
 \tag{8}
\]
Direct substitution gives
\[
 e=(x_0^{-1}-K)\pi,\qquad f\pi=1-e^t,\qquad
                         G(\pi,1)^T=x_0^{-1}(\pi,1)^T .
 \tag{9}
\]
For example its lower entry is
\(f(K\pi+e)+K^{-1}=f\pi/x_0+e^t/x_0=x_0^{-1}\).

Put \(B_{-,j}=b_{-,j}\cdots b_{-,1}\), and set
\[
 v_j=B_{-,j-1}^{-1}(\pi_j,1)^T,\qquad
                    \mu_j=-B_{-,j-1}^{-1}G_jB_{-,j-1}.
 \tag{10}
\]
Then \(\mu_jv_j=M^{-1}v_j\).
At the original highest cut, both fields vanish by [R], so
\(\pi_1=0\) and \(v_1=(0,1)^T\). This vector uses the opposite
peripheral eigenline from (1). Its normalization is regular
there, and this distinction will be retained to the end.

## 3. Signed local transport with all occupation values retained

At one crossing let \(a,b,n\) be its analytic input occupations
and transfer, in the conventions of [E] and [R]. Put
\[
                      A=e^a,\qquad B=e^b,\qquad C=e^n .
 \tag{11}
\]
Define the analytic units
\[
 \tau_+=\frac{BC}{x_0}\frac{1-Y/A}{1-YC/A},
       \qquad
 \tau_-=\frac{x_0}{A}\frac{1-Y/B}{1-YC/B}.
 \tag{12}
\]
Every denominator is nonzero near the node's zero field point
because \(\alpha\ne1\). These are the local expressions of [Q],
but we check their extension to the present cut.

For a positive crossing, use [R]'s implicit variables
\(N,C_0,B_0\), with input occupations \(N+C_0,B_0\).
Write \(s=N+C_0\). Its last local equation [R, (8)] gives
\[
 \frac{1-e^{C_0}}{Z_2}
  =\frac{e^{B_0}}{x_0}
       \frac{1-e^s/Y}{1-e^{C_0}/Y}
                  \,p_1\frac{1-e^s}{s}.
 \tag{13}
\]
Here \(p_1\) is the input coherent momentum. The last factor is
exactly the input \(\pi_1\). Also
\[
 \frac{1-e^s/Y}{1-e^{C_0}/Y}
     =e^N\frac{1-Ye^{-s}}{1-Ye^{-C_0}} .
 \tag{14}
\]
Thus the output over-strand coordinate is \(\pi'_2=\tau_+\pi_1\).
Although the left quotient in (13) was written on a dense set,
(7) defines it holomorphically everywhere in this chart.

For a negative crossing, [R, (12)] in the same way gives
\[
 \frac{1-e^{C_0}}{Z_1}
    =x_0e^{-A_0}
       \frac{1-Ye^{-s}}{1-Ye^{-C_0}}
                     \,p_2\frac{1-e^s}{s},\qquad s=N+C_0 .
 \tag{15}
\]
It is \(\pi'_1=\tau_-\pi_2\).
These are identities of analytic functions, including zero
occupation coordinates.

The conserved triangular products and Hurwitz identities of [R]
now give the full global-vector transport at either sign:
\[
 v'_{\rm under}=-\mu_{\rm over}^{-\epsilon}v_{\rm under},
       \qquad
 v'_{\rm over}=\tau_\epsilon v_{\rm over},
                    \qquad \epsilon\in\{1,-1\}.
 \tag{16}
\]
For the positive underpass this can be checked without any scalar
division: \(G_1^{-1}b_{-,1}^{-1}=b_{+,1}^{-1}\), and the second
row of \(b_{+,1}^{-1}\) is \((0,1)\). It therefore sends the
normalized incoming eigenvector to the normalized outgoing one.
The overpass follows from (13) and the conserved product;
their first components fix the scalar on a dense open set.
For the inverse crossing use the inverse identities of [R]
or (15); this reverses the meridian power in (16).
All vectors and matrices in (16) are holomorphic, so the dense
identities extend through their zero components. The same
earlier-strand prefixes conjugate each two-strand calculation.

## 4. Closing the vector transport fixes the preferred longitude

Follow the single oriented knot from the cut back to itself.
Let \(c_\times\) be its total crossing count, and let \(W\)
be the left-ordered product of \(\mu_{\rm over}^{-\epsilon}\)
encountered at underpasses. Scalars at overpasses commute with
these matrices. Since the normalized vector returns to itself,
(16) gives
\[
             1=(-1)^{c_\times}T_{\rm over}\,
                      \operatorname{eig}_{M^{-1}}(W),
          \qquad T_{\rm over}=\prod_{\rm crossings}\tau_\epsilon .
 \tag{17}
\]
In the diagram convention of [Q], the oriented blackboard parallel
has holonomy \(W^{-1}\): pushing the parallel along the diagram
records the over-meridians with their crossing signs, in the
inverse order to the left-ordered vector transport. Its linking
number with the knot is the writhe \(w\). Removing that writhe
gives the preferred longitude
\[
                              \lambda=W^{-1}\mu_1^{-w}.
 \tag{18}
\]
This also shows explicitly why the writhe correction is required.

On the \(M^{-1}\) line, (17)--(18) give
\[
 \operatorname{eig}_{M^{-1}}(\lambda)
      =(-1)^{c_\times}M^w T_{\rm over}=x_0^w T_{\rm over},
 \tag{19}
\]
since \(c_\times\equiv w\pmod2\) and \(M=-x_0\).
The commuting longitude has determinant one. Therefore its value
on the highest \(M\) line in (1) is
\[
                              \ell=x_0^{-w}/T_{\rm over}.
 \tag{20}
\]

## 5. Comparison with the actual meridian row

Let \(c=b+n\) at a positive crossing and \(c=b-n\) at a
negative crossing; here \(c\) is the left output occupation,
not the source framing exponent. The local contributions
to \(\mathcal R\) in [E] are
\[
 R_+=e^{(-a-b+n)/2}\frac{1-Y^{-1}e^{a-n}}{1-Y^{-1}e^a},
 \qquad
 R_-=e^{(a+b-n)/2}\frac{1-Ye^{n-b}}{1-Ye^{-b}} .
 \tag{21}
\]
The expressions (12) satisfy, exactly,
\[
       R_+=e^{(c-a)/2}x_0^{-1}\tau_+^{-1},\qquad
       R_-=e^{(c-a)/2}x_0\tau_-^{-1}.
 \tag{22}
\]
For the first identity use
\((1-Y^{-1}A/C)/(1-Y^{-1}A)
  =C^{-1}(1-YC/A)/(1-Y/A)\).
The second follows directly.

There is no square-root ambiguity in the product of the
exponentials in (22). Let \(J=-\sum_j j\,t_j\) on a braid
stage, where \(t_j\) is its analytic occupation. At either
crossing, exact conservation of the sum of its two occupations
gives \(J_{\rm out}-J_{\rm in}=c-a\).
Every strand occupation closes, including the zero cut, by [R].
Hence \(\sum(c-a)=0\) as an additive identity. Multiplying
(22) yields
\[
        \mathcal R(Y,e^{\Theta_g})
               =x_0^{-w}/T_{\rm over}=\ell .
 \tag{23}
\]
The clock evaluations here are the actual stage occupations
proved in [R], with the same linear specialization to matching
coordinates. No factor in the finite source row has been
discarded: the above comparison is of its complete classical
coefficient.

The second equality in (3) is the actual-minor identity of [H].
Both logarithms vanish at \(Y=\alpha\), since \(S_g=O(z^2)\).
Taking their analytic logarithms proves (4).

## 6. Why this is an A-polynomial germ

We record the local dimension argument to avoid assuming that an
arbitrary analytic curve in a representation variety is algebraic.
Fix a sufficiently small \(z\ne0\) on the constructed branch.
Nearby representations can have their ordered cut eigenlines
placed at the two coordinate lines; the remaining conjugation
is the diagonal group.

Gauss reconstruction is regular here. If
\(P_j=H_j\cdots H_1\), its upper-left entry is close to \(x_0^j\)
and is nonzero. Its unique triangular factors are
\[
 B_-(P_j)=
  \begin{pmatrix}1&0\\-(P_j)_{21}&(P_j)_{11}\end{pmatrix},
 \qquad
 B_+(P_j)=
  \begin{pmatrix}(P_j)_{11}&(P_j)_{12}\\0&1\end{pmatrix}.
 \tag{24}
\]
They satisfy \(P_j=B_-(P_j)^{-1}B_+(P_j)\).
Successive quotients recover the individual \(b_{\pm,j}\).
The field chart (6) is invertible near its zero point by [R].
Thus nearby knot representations in this frame are exactly
the full coherent stationary solutions, not merely a subset.

For \(z\ne0\) those equations are
\(P=C\mathcal P_Z,\ Z=C^T\mathcal P_P\), as in [R].
Set \(A=u^T\mathcal P_P/z\) and
\(B_s=v^T\mathcal P_Z/z\). They recover the hard equations
uniquely, and the soft equations are
\[
              A(\Psi_x-z)=B_s(\Psi_x-z)=0 .
 \tag{25}
\]
On this irreducible branch \(A B_s\ne0\).
The diagonal conjugation is precisely
\((A,B_s)\mapsto(tA,t^{-1}B_s)\).
Its quotient is the variable \(x=AB_s\), and its remaining
equation is \(\Psi_x=z\).
The derivative in \(x\) is \(2\sigma+O(z)\ne0\).
Consequently this is a smooth one-dimensional character germ,
with \(Y\) a local coordinate.

The representation equations, preferred peripheral word and
eigenvalue conditions are polynomial after adjoining \(M\)
and clearing invertible matrix determinants. The above germ
therefore belongs to a one-dimensional algebraic character
component; its peripheral image is a curve, since its meridian
is nonconstant. By the definition of the nonabelian A-polynomial
image, that curve supplies a factor of \(A_K(M,L)\).
Equations (3) and (23) give (5). Inclusion or omission of the
separate abelian factor \(L-1\) in the naming convention does
not affect this assertion.

The proof fixes the preferred longitude and shows that the
source-selected local action lies on that A-curve. It supplies
neither a geometric-component label nor a volume evaluation.

## 7. Complete written proof directs

| Label | Complete proof source | SHA256 |
|---|---|---|
| H | notes/research_actual_minor_quantum_meridian_action.md | 07b219d56ad42157ae6b2282c5bc0a73f3baf79c0c5dfc17fa07dfe145d2e822 |
| R | notes/research_principal_critical_highest_cut_representation.md | d77b2193d34c0e174389cfdf3d52e34f6ab59f61f2d5263842b65a6769e7d9d4 |
| E | notes/research_actual_quantum_meridian_clock_connection.md | 883a4526e8db3e666f8f962b8eb5311700afbc7813b1b74b16be03bcdac3e865 |
| Q | notes/quantum_longitude_and_regulator_action.md | e8ac5dc6bab05be0dad3810311dc3a8b169ad810b898aa3db75582087dbe8aa7 |

H supplies the actual action/clock equation; R supplies the same
selected representation, field chart, full cut closure and mark
observables. E supplies the original finite-row coefficients.
Q fixes the diagram's preferred parallel convention and provides
the local vector-transport formulas rederived here in a chart
regular at the original highest cut. No averaged-cut or geometric
regulator assertion is a premise. The regular eigenvector, full
monomial telescoping, preferred eigenflag and local algebraic
curve argument are proved above.

Only written mathematics, source-text reads and hash checks were used.
Frozen manuscripts and public documentation are unchanged.
