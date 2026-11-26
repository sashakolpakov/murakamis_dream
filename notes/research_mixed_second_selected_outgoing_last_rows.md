# The outgoing last row at the second selected coordinate

Research theorem, 6 November 2026.

When the second retained coordinate is selected, the last-row profile
of the factor to its right decreases as that coordinate moves from its
negative reference height to a positive height. This decrease pays for
the growth of each main or cut profile of the factor to its left.
The proof uses the original unselected comparisons and elementary
argument bounds. It needs no new parameter cover.

The result removes six of the thirty-two terms in
[the second-selection reduction](research_mixed_second_selected_plateau_reduction.md).
It does not include the two Fourier alternatives for the pair of two
last-row profiles, the other twenty-four terms, or the case where both
first coordinates are selected.

## 1. The profiles and their original supporting planes

Fix an actual positive three/four word of length \(m\ge4\), with
\((\epsilon_1,\epsilon_2,\epsilon_3)=(\alpha,1,\beta)\) and
\(\alpha,\beta\in\{0,1\}\). Position 1 is unselected. Write
\[
 r_j=a_j+ic_j,\qquad c=c_2<0,\qquad
 z_1=x_1+ic_1,\quad z_k=y+ik,\quad z_3=x_3+ic_3,
 \qquad x_1,y,x_3\in P=[.22,.45].
 \tag{1}
\]
Only \(k\) changes. Its final value throughout this note is
\[
                         H=\frac1{100}.
 \tag{2}
\]
The ordinary index of factor 2 retains its actual imaginary part
on its main contour. For that factor put
\[
 Q(s;z_1,z)=g(s+z_1)+g(s+z)-3g(s)-g(z_1)-g(z)+2\pi iz_1s.
 \tag{3}
\]
Here \(g'(w)=\log(1-e^{-2\pi iw})\) on the original regular
strip, with the original primitive normalization. Define
\[
 \begin{split}
 L_0^k&=\max_{1/8\le x\le1/2}\Re Q(x+i\Im s_2^*;z_1,z_k),\\
 L_L^k&=\Re Q(1/8;z_1,z_k),\qquad
 L_R^k=\Re Q(1/2;z_1,z_k),\\
 T^k&=2\pi(-k)_++2\pi(c_3)_+,\qquad
 G_k(y)=\Re g(y+ik),\\
 J(y)&=G_0(y)=\int_0^y\log(2\sin\pi t)\,dt .
 \end{split}
 \tag{4}
\]
Thus \(L_i^k\) is the profile \(R_i^2\) of the reduction, and
\(T^k\) is its full periodic last-row profile \(R_1^3\).
In particular \(T^k\) is not a central-branch evaluation at index one.

Retain the original action \(M_{23}\), marginals \(p_L,p_R\),
and affine function
\[
 \Lambda_{23}=M_{23}
       +\Re p_L(x_1-a_1)+\Re p_R(x_3-a_3).
 \tag{5}
\]
Set \(d_1=x_1-a_1\), \(d_2=y-a_2\), \(d_3=x_3-a_3\), and
\(\kappa=1/2500000\). The individual unselected current comparisons give
\[
 L_i^c+T^c-G_c(y)
       -\frac{\alpha}{2}\Re g(z_1)-\frac{\beta}{2}\Re g(z_3)
 \le \Lambda_{23}-\kappa(d_1^2+2d_2^2+d_3^2),
                 \qquad i=0,L,R.
 \tag{6}
\]

Here is the source of this assertion. Section 2 of
[the ordinary source assembly](research_mixed_three_row_source_assembly.md)
proves each main, left-cut, half-row, and last-row comparison before
combining them into the finite-kernel bound. Apply its main, left-cut,
or half-row inequality to factor 2, with allocations
\(-\alpha g(z_1)/2-g(z_c)/2\). Apply its last-row inequality to
factor 3, with allocations \(-g(z_c)/2-\beta g(z_3)/2\).
Both factors are ordinary when \(m\ge4\); the adjacent attached
inputs at \(m=4\) are included in that assembly's domain check.
Their constants add to \(M_{23}\), the two derivatives in \(z_c\)
cancel by the original stationary equation, and their other
derivatives give (5). Their quadratic terms give (6).
This uses inequalities for individual profiles, not an inference
from the modulus of a cancelling sum.

## 2. Moving the shared coordinate

For \(0<t<1\), define
\[
 A(t,k)=\arg(1-e^{2\pi k-2\pi it})
 \tag{7}
\]
with the same regular-strip logarithm as in (3). The elementary
radius bounds are
\[
 \pi\min(1-2t,0)\le A(t,k)\le\pi\max(1-2t,0).
 \tag{8}
\]
When \(0<t<1/2\) and \(k\le0\), the sharper bound is
\[
                     0\le A(t,k)\le\pi(1/2-t).
 \tag{9}
\]
These are the original argument bounds used in
[the first-selection last-row proof](research_mixed_selected_four_three_last_rows.md).
They hold at every height occurring here.

Fix \(s=x+ih\), \(1/8\le x\le1/2\), and put
\(\Phi_s(k)=\Re Q(s;z_1,y+ik)\). The shared argument is outgoing
in factor 2, so its chirp is independent of \(k\). Consequently
\[
 \Phi_s'(k)=A(y,k)-A(x+y,h+k),\qquad
 G_k'(y)=-A(y,k).
 \tag{10}
\]
All arguments remain regular: \(y\in P\) and
\(.345\le x+y\le.95\).

**Lemma 1.** Uniformly in these variables,
\[
 \begin{array}{c|c|c}
 &c\le k\le0&0\le k\le H\\ \hline
 \Phi_s'(k)&\le19\pi/20&\le\pi\\
 (\Phi_s-G)'(k)&\le\pi&\le39\pi/25 .
 \end{array}
 \tag{11}
\]

*Proof.* If \(x+y\ge1/2\), equations (8)--(9) give on the
negative part of the path
\[
 \Phi_s'\le\pi(2x+y-1/2)\le19\pi/20,\qquad
 (\Phi_s-G)'\le2\pi x\le\pi.
 \tag{12}
\]
On the positive part they give
\[
 \Phi_s'\le2\pi x\le\pi,\qquad
 (\Phi_s-G)'\le\pi(1+2x-2y)\le39\pi/25.
 \tag{13}
\]
If \(x+y<1/2\), the subtracted argument in (10) is nonnegative.
Dropping it gives the four upper bounds
\(7\pi/25,14\pi/25,14\pi/25,28\pi/25\), respectively.
Each is no larger than its corresponding bound in (11). The
argument is zero when \(x+y=1/2\). This proves the table.
\(\square\)

The estimate holds for every point of the original main line and
both real cuts, so it remains valid after the maximum defining \(L_0\).
In particular
\[
 \begin{split}
 L_i^H-G_H-2\pi H-(L_i^c-G_c)
       &\le-\pi c-\frac{11\pi}{25}H,\\
 L_i^H-L_i^c&\le-\frac{19\pi}{20}c+\pi H,
                          \qquad i=0,L,R.
 \end{split}
 \tag{14}
\]
The neighboring last row has the exact change
\[
                           T^H-T^c=2\pi c.
 \tag{15}
\]

## 3. Both Fourier alternatives have a strict gap

The full selected weight has the two rates
\[
 W_{\mathrm{fac}}=-G_H(y)-2\pi H,\qquad
 W_{\mathrm{force}}=0.
 \tag{16}
\]
Define the six allocated profiles
\[
 E_{i,\nu}=L_i^H+T^H+W_\nu
       -\frac{\alpha}{2}\Re g(z_1)-\frac{\beta}{2}\Re g(z_3),
 \quad i=0,L,R,\quad \nu\in\{\mathrm{fac},\mathrm{force}\}.
 \tag{17}
\]

**Theorem 2.** For every reference and target in (1), all six profiles satisfy
\[
 E_{i,\nu}<
 \Lambda_{23}-\kappa(d_1^2+2d_2^2+d_3^2)-\frac1{400}.
 \tag{18}
\]
The constant is independent of the word length and of \(\alpha,\beta\).

*Proof.* For the factorial alternative, (14)--(15) show that its
change relative to the left side of (6) is at most
\[
                  \pi c-\frac{11\pi}{25}H
                     <-\frac{11\pi}{2500}<-\frac1{400}.
 \tag{19}
\]
For the forced alternative the change is at most
\[
                  \frac{21\pi}{20}c+\pi H+G_c(y).
 \tag{20}
\]
By (9),
\[
 G_c(y)=J(y)+\int_c^0 A(y,k)\,dk
              \le J(y)-\pi(1/2-y)c.
 \tag{21}
\]
Thus (20) is at most
\[
 \pi H+J(y)+\pi(11/20+y)c<\pi H+J(9/20).
 \tag{22}
\]
Here \(c<0\), and \(J\) increases on \(P\), because
\(2\sin\pi y>1\) there.

For completeness the remaining numerical constant has an exact
elementary proof. Since \(J(1/2)=0\) and the logarithmic integrand
increases on \([9/20,1/2]\),
\[
 J(9/20)\le-\frac1{20}\log(2\cos(\pi/20))<-\frac{17}{500}.
 \tag{23}
\]
Indeed \(\pi<22/7\) and \(\cos t\ge1-t^2/2\) give
\(2\cos(\pi/20)>9679/4900\). For \(x=17/25\), the positive
exponential series with a geometric bound on its tail gives
\[
 e^x\le\sum_{j=0}^5\frac{x^j}{j!}
        +\frac{x^6}{6!}\frac1{1-x/7}
       =\frac{2192855025919}{1110937500000}
       <\frac{9679}{4900}.
 \tag{24}
\]
The last difference is exactly \(77744354969/54435937500000>0\).
This proves the strict logarithmic inequality in (23).
Combining (22)--(23) with (2) yields a deficit greater than
\[
                  \frac{17}{500}-\frac{11}{350}
                    =\frac9{3500}>\frac1{400}.
 \tag{25}
\]
Together with (6), this proves (18). \(\square\)

## 4. The resulting finite-source reduction

In the defect \(\mathfrak D_{23}\) of the second-selection reduction,
remove the six terms with left profile \(0,L,R\) and right profile
1. Let \(\mathfrak D_{23}^{\mathrm{rem}}\) be the maximum over
the remaining twenty-six terms, retaining both Fourier alternatives.
Theorem 2 and the full finite-current reduction imply
\[
 \mathcal B_{23,N}\le C_\tau N^{A_\tau}
  \exp N\left\{\Lambda_{23}
    +\max\left(-\frac1{400},
                   \mathfrak D_{23}^{\mathrm{rem}}\right)+\tau\right\}.
 \tag{26}
\]
Both level parities and all original rows remain included in this
bound. A total rate tolerance less than \(1/800\) leaves a gap
\(1/800\) for the six removed profiles. No positivity of finite
coefficients has been assumed.

The two-last-row pair is still among the twenty-six terms. Its left
profile is \(2\pi(-c_1)_++2\pi k_+\), which does not have derivative
(10), so the present argument cannot be applied to it. Nor does (26)
bound the other terms by a negative constant. Their signs, the case
where position 1 is also selected, and the full-source comparison
remain open.
