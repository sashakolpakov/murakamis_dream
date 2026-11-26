# A contour determined by the smallest neighboring cutoff

Research proof, 4 November 2026. This changes the contour outside the
already controlled low and central regions. The finite Laurent sum and
its normalization are unchanged. The construction gives a smaller
bound for changes in height when several transition coordinates are
adjacent. It does not establish the missing finite-sum estimates there.

## 1. The contour and the exact integral

Use the cutoff
\[
 \rho(x)=
 \begin{cases}
 0,&0\le x\le1/10,\\
 (25/3)(x-1/10),&1/10\le x\le11/50,\\
 1,&11/50\le x\le9/20,\\
 20(1/2-x),&9/20\le x\le1/2,\\
 0,&1/2\le x\le1,
 \end{cases}                                                   \tag{1}
\]
extended periodically. Fix a cyclic three/four word of length
\(m\ge1\), its original geometric coordinates \(r_j\), and a
subset \(S\) of the four-type positions. As in the
[all-selection theorem](research_mixed_selected_low_plateau_clusters.md),
let \(c_j=\Im r_j\) when \(j\notin S\), and \(c_j=7/500\)
when \(j\in S\). Define
\[
 H_j(x)=c_j\min\{\rho(x_{j-1}),\rho(x_j),\rho(x_{j+1})\}.
                                                               \tag{2}
\]
Cyclic subscripts may coincide. A repeated entry in the minimum has
no extra multiplicity.

The graph is continuous, periodic and piecewise affine, with finitely
many pieces. At almost every point, each row of \(DH\) has at most
one nonzero entry. Its absolute value is at most
\(20\max|c_j|\le57/50\). This remains true on open regions where
several entries of the minimum are the same constant. The other tie
sets have measure zero. Hadamard's inequality therefore gives
\[
 |\det(I+iDH)|
 \le\{1+(57/50)^2\}^{m/2}<(38/25)^m.                          \tag{3}
\]
The [exact coupled-contour identity](research_mixed_coupled_outer_graph.md)
applies to each original selected Laurent term \(\mathcal D_{N,S}\):
\[
 \operatorname{CT}\mathcal D_{N,S}
 =\int_{\mathbb T^m}
   \mathcal D_{N,S}(e^{-2\pi i(x+iH(x))})
                   \det(I+iDH(x))\,dx.                        \tag{4}
\]
This is an identity at every finite level. In particular it includes
the actual Fourier polynomials and all factors \(X_j^{-N}\).

Put \(L=[0,.10]\), \(P=[.22,.45]\). On \((L\cup P)^m\),
all cutoff values are zero or one, so their minimum equals their
product. Thus (2) agrees exactly with the previously proved contour
there, and its Jacobian is one almost everywhere on these boxes.
The entire conclusion of the all-selection theorem transfers:
every box containing a low coordinate loses at least \(1/100\)
in exponential rate, every nonempty selection on \(P^m\) loses
at least \(1/200\), and the retained central term has its original
nonzero coefficient and power \(N^0\).

If \(\rho(x_j)=0\), then \(H_{j-1}=H_j=H_{j+1}=0\).
An isolated transition coordinate with distinct neighboring plateau
coordinates gives the same three heights as the product contour.
This last observation does not identify the two graphs at intermediate
cutoffs for cycles of length one or two. Equation (4) and the transfer
on \((L\cup P)^m\) hold for those lengths without an exception.

## 2. A common convex domain for the critical equations

On \([.1,.5]\), the function \(\rho\) is concave: its successive
slopes are \(25/3,0,-20\). Define
\[
 \begin{split}
 D_3&=\{x+ih:.1\le x\le.5,
                    -.03\rho(x)\le h\le.02\rho(x)\},\\
 D_4&=\{x+ih:.1\le x\le.5,
                    -.057\rho(x)\le h\le.014\rho(x)\}.
 \end{split}                                                   \tag{5}
\]
Both are compact convex polygons. All targets of (2) with real
coordinates in this interval belong to their respective polygons.
The original reference rectangles belong to them as well. Consequently
every straight reference-to-target segment stays in their product.

These polygons lie strictly inside the allowed imaginary cotangent
strip. Indeed
\[
 |\Im\cot\pi(x+ih)|
 =\frac{|\sinh(2\pi h)|}{\cosh(2\pi h)-\cos(2\pi x)}
 \le\frac{\rho(x)\sinh(57\pi/500)}{2\sin^2(\pi x)}.           \tag{6}
\]
We used \(|h|\le.057\rho(x)\), convexity of \(\sinh\) on
the positive axis and its value zero at the origin. For
\(.1\le x\le.22\), the exact identity
\[
 \frac{125}{6}x^2-\frac{25}{3}(x-1/10)
                    =\frac{125}{6}(x-1/5)^2                   \tag{7}
\]
and the decreasing function \(\sin t/t\), \(0<t\le\pi/2\),
give
\[
 \frac{\rho(x)}{\sin^2(\pi x)}
 \le\frac{121}{120\sin^2(11\pi/50)}.
\]
For \(.22\le x\le.5\), use \(\rho\le1\) and the increasing
sine instead. The resulting uniform bound is
\[
 |\Im\cot\pi(x+ih)|
 \le\frac{121\sinh(57\pi/500)}{240\sin^2(11\pi/50)}
 <\frac{23}{50}<\frac12.                                     \tag{8}
\]
The last strict inequality is certified by directed real arithmetic.
Also \(\Re\cot\pi(x+ih)\ge0\), with equality only at
\(x=.5\), where (5) forces \(h=0\).

The [closed cotangent theorem](research_mixed_closed_cotangent_roots.md)
therefore gives the unique original conditional root, its zero
logarithmic lift, and positive negative-real Schur Hessian on every
typed product \(D_{3+\eta}\times D_{3+\epsilon}\).
All are uniform on these compact products. This is a conclusion about
the critical phase. A finite-source asymptotic or upper bound on the
whole polygons is a separate requirement.

## 3. A dimension-independent bound for the height displacement

Take the unselected graph, so \(c_j=h_j^*=\Im r_j\), and suppose
\(x\in[.1,.45]^m\). Write \(a_j=\Re r_j\) and
\(d_j=x_j-a_j\). At each row choose an index
\(i(j)\in\{j-1,j,j+1\}\) where the cutoff is smallest.
If that value is one, the row has no height displacement. Otherwise
\(x_{i(j)}<.22<a_{i(j)}\), and
\[
 H_j(x)-h_j^*
       =h_j^*\lambda_{i(j)}d_{i(j)},\qquad
 \lambda_i=\frac{1-\rho(x_i)}{a_i-x_i}.                        \tag{9}
\]
The lower bounds \(a_i\ge.30\) for type three and
\(a_i\ge.27\) for type four imply
\[
 0\le\lambda_i\le
 \begin{cases}5,&i\text{ has type three},\\100/17,&i\text{ has type four}.
 \end{cases}                                                   \tag{10}
\]
To see this, the ratio \((.22-x)/(.12(a_i-x))\) decreases on
\([.1,.22]\) and has maximum \(1/(a_i-.1)\).

Thus (9) has the form \(H-h^*=Cd\), where every row of the real
matrix \(C\) has at most one nonzero entry, each column has at most
three, and \(|C_{ji}|\le57/170\). Repeated cyclic indices decrease
the number of distinct rows assigned to a column. Directly,
\[
 \begin{split}
 \|H-h^*\|_2^2
 &\le(57/170)^2\sum_j|d_{i(j)}|^2\\
 &\le3(57/170)^2\|d\|_2^2
 \le\frac9{25}\|d\|_2^2.
 \end{split}                                                   \tag{11}
\]
This holds for every fixed word length, including one and two,
and does not sample the original critical coordinates.

Equations (5) and (11) restrict the straight displacements that need
to be considered in a global phase comparison. They do not say that
the phase is concave after substituting (2): positive ambient
curvature alone does not give such a statement. The required estimate
is still a bound for the real Hessian quadratic on these coupled
displacements, together with a bound for the complete finite source.
The selected terms require their actual Fourier penalties as well.

## 4. Reproduction

    python3 experiments/check_mixed_minimum_neighbor_contour.py

The checker verifies the exact cutoff and displacement constants,
the strict cotangent enclosure, and the low/plateau equality for all
binary cyclic patterns through length ten. The arbitrary-length
incidence argument and the exact contour identity are proved above.
