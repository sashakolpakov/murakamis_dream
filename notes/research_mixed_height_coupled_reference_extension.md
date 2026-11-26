# A boundary estimate for references with coupled target heights

Research lemma, 4 November 2026. This is an analytic maximum-principle
estimate, not a completed right-transition source comparison. It repairs
the specific loss of harmonicity when a target height is a fraction of
the reference height. No completed source artifact is changed.

## 1. The exact Laplacian

Let \(\mathcal R=R_1\times\cdots\times R_k\) be a product of closed
complex rectangles, and let \(z:\mathcal R\to\mathbb C^n\) be
holomorphic on a neighborhood. Let \(F\) be holomorphic on neighborhoods
of both its reference image and the target image below. Its Hessian is
complex symmetric. Fix a real vector \(x\), a real number
\(0\le\tau\le1\), and nonnegative constants \(d_j\). Set
\[
 w=x+i\tau\Im z,
 \qquad
 D=\Re\{F(w)-F(z)-F'(z)\cdot(w-z)\}
       +(1-\tau)^2\sum_jd_j(\Im z_j)^2.
 \tag{1}
\]
The parameters \(x,\tau\) are held fixed when a reference variable is
differentiated. In particular, a real cutoff \(\tau=20(.5-t)\) is
allowed when \(t\) is a fixed target coordinate, independently of
the reference.

For the \(\ell\)-th complex reference variable \(p_\ell\), write
\(q=\partial_{p_\ell}z\) and
\(\Delta_\ell=\partial_{\Re p_\ell}^2+
\partial_{\Im p_\ell}^2\). Then
\[
\begin{split}
 \Delta_\ell D={}&
 -\tau^2\Re\{q^TF''(w)\overline q\}
 +2\tau\Re\{q^TF''(z)\overline q\}\\
 &+2(1-\tau)^2\sum_jd_j|q_j|^2.
\end{split}
 \tag{2}
\]

To verify the formula, use
\(w=x+(\tau/2)(z-\overline z)\),
\(\partial_p w=\tau q/2\), and
\(\partial_{\overline p}w=-\tau\overline q/2\).
Differentiating the first line of (1) once in each Wirtinger variable
gives (2), since \(\Delta=4\partial_p\partial_{\overline p}\).
Terms holomorphic only in \(z\) have zero Laplacian, and
\(\Delta(\Im z_j)^2=2|q_j|^2\). There are no second derivatives
of the reference map in (2).

Suppose the target real Hessian satisfies
\[
                         -\Re F''(w)\succeq0.              \tag{3}
\]
The first term of (2) is nonnegative. Indeed, if \(A=-\Re F''(w)\)
and \(q=u+iv\), symmetry gives
\(\Re(q^TF''(w)\overline q)=-u^TAu-v^TAv\).
The last term of (2) is also nonnegative. Consequently
\[
 \Delta_\ell D\ge-2\tau B_\ell,
 \qquad
 B_\ell\ge
 \sum_{i,j}|q_iq_jF''_{ij}(z)|.                            \tag{4}
\]
The repeated entries of the symmetric Hessian are both counted.

## 2. Extending a boundary gap with a quantified cost

Let \(h_\ell\) be the imaginary width of \(R_\ell\). Assume that
the constants \(B_\ell\) in (4) hold throughout \(\mathcal R\),
and that
\[
 D\le-\gamma
 \quad\text{on}\quad
 \partial R_1\times\cdots\times\partial R_k.              \tag{5}
\]
Then everywhere in \(\mathcal R\),
\[
                 D\le-\gamma+
                   \frac{\tau}{4}\sum_{\ell=1}^kB_\ell h_\ell^2.
 \tag{6}
\]
Thus the boundary gap persists if the last sum is strictly smaller
than \(\gamma\). The real width may replace the imaginary width
in any coordinate; the smaller width gives the better bound.

For a direct proof, write \(R_\ell\)'s imaginary interval as
\([a_\ell,b_\ell]\) and put
\[
 v_\ell=\tau B_\ell
       (\Im p_\ell-a_\ell)(b_\ell-\Im p_\ell).
 \tag{7}
\]
Then \(v_\ell\ge0\),
\(\Delta_\ell v_\ell=-2\tau B_\ell\), and
\(v_\ell\le\tau B_\ell h_\ell^2/4\).
The function \(D-\sum v_\ell\) is separately subharmonic.
On the distinguished boundary it is no greater than \(D\),
so successive maximum principles prove (6). Both reference costs
are retained when there are two external variables.
The same estimate holds uniformly over any compact set of fixed
real targets \(x\) and fractions \(\tau\) for which its hypotheses
hold; apply the argument to each target before taking a supremum.

There is a legitimate boundary reduction for the constants in (4):
each \(q_iq_jF''_{ij}(z(p))\) is holomorphic on the whole reference
product. Hence their sum of absolute values is separately subharmonic
and its maximum is attained on the distinguished boundary. This
requires the independently established whole-product branch first.
It does not assert that the defect \(D\) itself is subharmonic.
At \(\tau=0\), (2) does make \(D\) subharmonic and (6) has zero
extension cost, recovering the fixed-real-target argument.

## 3. Exact paired right-transition formulation

Use the original allocated phases and logarithmic branches of the
[full right-square source theorem](research_mixed_unselected_right_taper_products.md).
For three consecutive actual outer coordinates \(z=(a,b,c)\), set
\[
 F(a,b,c)=\phi_{\alpha\beta}(a,b)+\phi_{\beta\gamma}(b,c),
 \quad x=(p,t,q),\quad
 \tau=20(.5-t),\quad .45\le t\le.5,
 \quad p,q\in[.22,.45].                                   \tag{8}
\]
The two outside oriented reset debits are exactly the last term of
(1) for
\[
                         (d_1,d_2,d_3)=(151/20,0,11/2).
 \tag{9}
\]
The original stationary equation at the middle outer coordinate
gives \(F_b(z)=0\). Thus the complex affine term in (1) is precisely
the sum of the two original geometric supporting planes, including
all imaginary-coordinate contributions. This identity also holds on
an open window when its middle outer coordinate is internal; it is
not imposed on arbitrary independent reference triples.

The new geometric table in
[the neighbor-conditioned theorem](research_mixed_neighbor_conditioned_critical_boxes.md)
can sharpen a direct integrated-Hessian approach. Alternatively,
(6) permits a quantitative distinguished-boundary approach on a
longer open window, where derivatives of the middle coordinates
with respect to the external variables are smaller.
The following quantitative inputs remain to be proved before (6)
can yield a right-transition source theorem:

1. A boundary comparison (5) on every required external type product,
   uniformly in all real targets in (8), with the actual cutoff
   fraction retained.
2. Original target-branch existence and (3) on the whole reference
   product used in the extension, not only at actual cyclic points.
3. Constants \(B_\ell\) for that product with total cost in (6)
   smaller than the boundary gap.

The existing full finite-source packet may then be used at the actual
targets, with the true Fourier upper bound and a strictly smaller gap.
No such quantitative comparison, source promotion, or transition
assembly is claimed here. In particular, an uncorrected maximum
principle cannot replace (6) when \(\tau>0\).

Reproduction of the exact differentiation and barrier bookkeeping:

```sh
python experiments/check_mixed_height_coupled_reference_extension.py
```
