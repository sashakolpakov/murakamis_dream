# The complete right real-row tail is bounded by its endpoints

Research proof, 5 November 2026. At the common actual open-word height
bound \(|h_a|,|h_b|\le.108\), every real row between one half and
one is bounded by the half-row or the last row. The statement holds
throughout the independent horizontal plateau square. It retains the
original first chirp, all wrapped rows, and the original allocated
Fourier halfweights. Together with the asymmetric contour, this removes
the interior quartic/sextic candidates from the horizontal finite-source
upper bound. The calibrated inequalities at the remaining real rows
are separate obligations.

## 1. The original rate and the theorem

Let \(x,z\in P=[11/50,9/20]\), \(a=x+ih_a\),
\(b=z+ih_b\), and \(|h_a|,|h_b|\le27/250\). Use
\[
 \begin{split}
 E_\epsilon(u;a,b)
 &=\int_0^u\log|1-e^{-2\pi i(a+t)}|\,dt
   +\int_0^u\log|1-e^{-2\pi i(b+t)}|\,dt\\
 &\hspace{5mm}-(2+\epsilon)J(u)-2\pi h_a u,
                  \qquad 0\le u\le1,\quad\epsilon\in\{0,1\}.
 \end{split}
 \tag{1}
\]
All integrable logarithmic zeros are retained. The allocated rate is
\(\mathcal R_\epsilon=E_\epsilon-\eta\Re g(a)/2
-\epsilon\Re g(b)/2\); these added terms are constant in the row.

**Theorem 1.** On this whole domain,
\[
 \boxed{\quad
 \max_{1/2\le u\le1}\mathcal R_\epsilon(u;a,b)
 =\max\{\mathcal R_\epsilon(1/2;a,b),
                         \mathcal R_\epsilon(1;a,b)\}.
 \quad}
 \tag{2}
\]
This is a comparison of the complete absolute-row rates, not a lower
bound or a noncancellation claim for the finite sum.

It suffices to prove the theorem for \(\epsilon=0\).
Indeed \(J(u)\ge0\) on \([1/2,1]\) and
\(J(1/2)=J(1)=0\). With the row-independent halfweights
canceled, the exact increment identity is
\[
 \mathcal R_1(u)-\mathcal R_1(t)
   =\mathcal R_0(u)-\mathcal R_0(t)-J(u),
                  \qquad t\in\{1/2,1\}.
 \tag{3}
\]
Thus the own-type-four increment is no larger. Equation (3) does not
compare the two absolute allocated rates after changing a type.

## 2. Reflection and the small-angle comparison

Set \(x_0=11/50\), \(R_i=e^{-2\pi H_i}\), where
\(H_1=|h_a|\), \(H_2=|h_b|\). Write
\(G_R(t)=\Re g(t-iH)\) when \(R=e^{-2\pi H}\).
Let \(\chi_1=1\) when \(h_a<0\), and
\(\chi_2=1\) when \(h_b>0\), with zero otherwise.
At a zero height either convention gives the same formulas.
The exact reflection in the
[row-reflection theorem](research_mixed_right_tail_reflection.md) is
\[
 \begin{split}
 \Phi(v;x,z)&=E_0(1-v;x,z)-E_0(1;x,z)\\
 &=G_{R_1}(x-v)-G_{R_1}(x)
   +G_{R_2}(z-v)-G_{R_2}(z)
   +2J(v)+v(\chi_1\log R_1+\chi_2\log R_2).
 \end{split}
 \tag{4}
\]
The sign-dependent drift is fixed by the radii; it is not released as
an independent parameter.

We use three consequences of even radial log-arc monotonicity from
that theorem:

* For \(0\le v\le\min(x,z)\), \(\Phi(v;x,z)\le0\).
  In particular this settles every \(v\le x_0\).
* For \(x_0\le v\le1/2\), the relative half-row increment
  is bounded by the increment at \(x=z=x_0\):
  \[
  \Phi(v;x,z)-\Phi(1/2;x,z)
       \le\Phi(v;x_0,x_0)-\Phi(1/2;x_0,x_0).
  \tag{5}
  \]
* For \(x_0\le v\le2x_0\), there is also the pointwise bound
  \(\Phi(v;x,z)\le\Phi(v;x_0,x_0)\).
  Indeed an arc of length \(v\) is minimized when its center is
  closest to zero. Here its right endpoint satisfies
  \(x\ge x_0\ge v/2\), so that minimum occurs at \(x=x_0\),
  and likewise for \(z\).

The same arc principle, without an angular restriction on its center,
always gives
\[
 \Phi(v;x,z)\le
 -2G_{R_1}(v/2)-2G_{R_2}(v/2)+2J(v)
                    +v(\chi_1\log R_1+\chi_2\log R_2).
 \tag{6}
\]
It is the minimum arc centered at zero that is used in (6), not a
claim that the actual outer targets have been moved there.

The height bound ensures
\[
 R_i>r_0:=101/200.
 \tag{7}
\]
For an elementary verification, \(.216\pi<594/875\), and
\(e^t\le1+t+t^2/[2(1-t/3)]<200/101\) at
\(t=594/875\). No numerical enclosure is needed.

## 3. The derivative of the corner profile is unimodal

Write \(c=\cos(11\pi/25)\), \(s=\sin(11\pi/25)\).
Elementary sine and cosine bounds give
\(0<c<19/100<1/3\), \(s>49/50\). For
\(x_0\le v\le1/2\), define
\[
 f_R^\chi(v)=J(v)-G_R(x_0)-G_R(v-x_0)+\chi v\log R.
 \tag{8}
\]
Then \(\Phi(v;x_0,x_0)=f_{R_1}^{\chi_1}(v)
+f_{R_2}^{\chi_2}(v)\), and \(\Phi(x_0;x_0,x_0)\le0\)
because \(G_R(x_0)\ge J(x_0)\).

Put \(C_i=(R_i+R_i^{-1})/2\ge1\),
\(q=\cot\pi v\), \(A=C_1-c\), \(B=C_2-c\).
The sign of the corner second derivative is the sign of
\[
 N(q)=2ABq^3-3s(A+B)q^2
       +2(C_1C_2+2-3c^2)q-s(C_1+C_2+2c).
 \tag{9}
\]
This follows by adding
\[
 \frac{(f_{R_i}^\chi)''(v)}{\pi}
  =\frac{(C_i-c)\cot\pi v-s}
             {C_i-\cos(2\pi(v-x_0))}
\]
and clearing positive denominators and \(1+q^2\).
The drift has zero second derivative. At zero height the calculation
is on the open interval \(v>x_0\) and extends by continuity.

The derivative \(N'\) is nonnegative. Its quadratic discriminant
is nonpositive exactly when
\[
 4AB\{AB+c(A+B)+2s^2\}-3s^2(A+B)^2\ge0.
 \tag{10}
\]
Set \(t_i=C_i-1\ge0\), so \(A=1-c+t_1\),
\(B=1-c+t_2\). The left side of (10) is exactly
\[
 \begin{split}
 &4t_1^2t_2^2+4(2-c)(t_1^2t_2+t_1t_2^2)
 +(1-c)(1-3c)(t_1^2+t_2^2)\\
 &\qquad+2(1-c)(c+9)t_1t_2+4(1-c)^2(t_1+t_2),
 \end{split}
 \tag{11}
\]
which has nonnegative coefficients. Since \(q\) decreases as
\(v\) increases, (9) can change sign only from positive to
negative. Thus the corner first derivative increases and then
decreases, allowing either part to be empty.

On the last part \(2x_0\le v\le1/2\), the corner second
derivative is strictly negative. Indeed \(\cot\pi v<1/5\).
For \(t=v-x_0\in[.22,.28]\), (7) gives
\[
 \Re\cot\pi(t-iH_i)
  =\frac{\sin2\pi t}{C_i-\cos2\pi t}
  >\frac{49/50}{5/4+19/100}=\frac{49}{72}>\frac23.
 \tag{12}
\]
Here \(C_i<5/4\). The scalar estimates follow from
\(\sin(11\pi/25)=\cos(3\pi/50)>49/50\),
\(\cos(11\pi/25)<19/100\), and
\(\tan(3\pi/50)<1/5\), using the elementary Taylor bounds
and \(157/50<\pi<22/7\).

If \(\Phi'(1/2;x_0,x_0)\ge0\), unimodality shows that the
corner profile on \([x_0,1/2]\) is at most the larger of its
two endpoint values. If its value at \(1/2\) is nonnegative,
(5) bounds every relevant actual row by its half-row. If that value
is negative, the pointwise comparison in Section 2 bounds all
\(v\le2x_0\) by the last row. For \(v>2x_0\), (12) and
the nonnegative final derivative show that the corner profile is
increasing, so (5) again bounds the actual row by its half-row.
This proves (2) in this first case.

## 4. A negative final derivative forces two height contributions

It remains to suppose \(\Phi'(1/2;x_0,x_0)<0\). Put
\[
 D(R)=1+R^2+2cR,\qquad
 g_\chi(R)=\log2-\tfrac12\log D(R)+\chi\log R.
 \tag{13}
\]
The final derivative is \(g_{\chi_1}(R_1)+g_{\chi_2}(R_2)\).
If neither \(\chi_i\) is one, it is positive, since
\(D(R)\le2+2c<4\). If just one is one, it is also positive:
\(g_1\) increases in \(R\), \(g_0\) decreases, and
\[
 e^{2\{g_1(R_1)+g_0(R_2)\}}
 \ge\frac{4}{(5/4+c)(2+2c)}
 >\frac4{(29/20)(12/5)}>1,
 \tag{14}
\]
using \(R_1>1/2\). Therefore both \(\chi_i=1\).

Define
\(A(R)=g_1(R)\). As a function of \(t=\log R\),
\[
 A_t=\frac{1+cR}{D(R)}>0,\qquad
 A_{tt}=-\frac{R\{c(1+R^2)+2R\}}{D(R)^2}<0.
 \tag{15}
\]
For each \(0<v\le1/2\), the centered contribution
\[
 h_v(R)=-2G_R(v/2)+v\log R
 \tag{16}
\]
is increasing and strictly convex in \(\log R\). In fact
\[
 (h_v)_t=v+\frac1\pi\arg(1-Re^{-\pi iv})>0,\qquad
 (h_v)_{tt}=\frac{R\sin\pi v}
                  {\pi(1+R^2-2R\cos\pi v)}>0.
 \tag{17}
\]
Consequently \(h_v\), considered as a function of \(A\),
is increasing and convex.

The present case says \(A(R_1)+A(R_2)<0\), with
\(R_i\in[r_0,1]\). We have \(A(r_0)<0<A(1)\), and
(14) implies \(-A(r_0)<A(1)\). Increasing one or both
arguments until their sum is zero can only increase
\(h_v(R_1)+h_v(R_2)\). On that line its convexity shows that
the maximum occurs at the two extreme values
\(A(r_0),-A(r_0)\). If \(R_*\) is defined by
\(A(R_*)=-A(r_0)\), this proves
\[
 h_v(R_1)+h_v(R_2)\le h_v(r_0)+h_v(R_*)
                          <h_v(r_0)+h_v(r_1),
            \qquad r_1=43/50.
 \tag{18}
\]
For the last inequality, \(R_*<r_1\) follows from the exact
rational comparison
\[
 16r_0^2r_1^2>
 (1+r_0^2+2(19/100)r_0)(1+r_1^2+2(19/100)r_1).
 \tag{19}
\]
The right side increases with \(c\), so (19) implies
\(A(r_0)+A(r_1)>0\) for the actual \(c<19/100\).

## 5. One centered envelope pays every row in the second case

Combining (6) and (18) bounds every reflected row by
\[
 C(v)=-2G_{r_0}(v/2)-2G_{r_1}(v/2)
                        +2J(v)+v\log(r_0r_1),
                         \qquad 0\le v\le1/2.
 \tag{20}
\]
This envelope is nonpositive on its entire interval.
To prove that assertion, let
\(C_i=(r_i+r_i^{-1})/2>1\), \(S=C_0+C_1\),
\(P_0=C_0C_1\), and \(w=\cos\pi v\). The sign of
\(C''(v)\) is the sign of
\[
 N_*(w)=2w^3-3Sw^2+(4P_0+2)w-S.
 \tag{21}
\]
Indeed multiply \(C''/\pi\) by the positive quantity
\(2\sin\pi v(C_0-w)(C_1-w)\).
Now \(N_*''(w)=12w-6S<0\) on \([0,1]\),
\(N_*(0)=-S<0\), and
\(N_*(1)=4(C_0-1)(C_1-1)>0\). Thus there is exactly
one sign crossing. As \(v\) increases, \(C''\) changes from
positive to negative. Also \(C'(v)\to-\infty\) at zero,
whereas
\[
 C'(1/2)=\log\frac{4r_0r_1}
                      {\sqrt{(1+r_0^2)(1+r_1^2)}}>0,
 \tag{22}
\]
by the exact rational inequality
\(16r_0^2r_1^2>(1+r_0^2)(1+r_1^2)\).
Therefore \(C\) decreases and then increases; its maximum is
at zero or at \(1/2\).

We have \(C(0)=0\), and the other endpoint has a strict
negative rational bound. Set
\[
 \begin{split}
 U(R)&=\sum_{k=0}^{10}\frac{(-1)^kR^{2k+1}}{(2k+1)^2},\qquad
 t=\frac{1-r_0r_1}{1+r_0r_1},\\
 L(t)&=\sum_{k=0}^{4}\frac{t^{2k+1}}{2k+1}.
 \end{split}
 \tag{23}
\]
The alternating dilogarithm series and the positive atanh series give
\[
 \begin{split}
 C(1/2)
 &=\frac{\operatorname{Ti}_2(r_0)+\operatorname{Ti}_2(r_1)}{\pi}
                   -\operatorname{atanh}t\\
 &<\frac{U(r_0)+U(r_1)}{157/50}-L(t)<-\frac1{250}.
 \end{split}
 \tag{24}
\]
Here \(\operatorname{Ti}_2(R)=\sum_{k\ge0}
(-1)^kR^{2k+1}/(2k+1)^2\). The last comparison is a finite
rational inequality with \(r_0=101/200\), \(r_1=43/50\);
it involves no proposed root or floating value. The same is true
of (19), (22), and the elementary exponential bound (7).
It follows that \(C(v)<0\) for every \(v>0\). Equation
(20) therefore pays every row in the second case by the last row.
Together with Section 3 and the type comparison (3), this proves
Theorem 1.

## 6. Consequence for the original finite horizontal source

The common actual height bound used here follows from the
[ordinary block image bounds](research_mixed_cyclic_critical_height_bounds.md)
and the
[open endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md).
Ordinary type-three and type-four heights lie inside
\((-.065,.068)\) and \((-.102,-.001)\); the attached endpoint
height bound is at worst \(-.108\), and the private endpoint
bounds are smaller in modulus. Thus the fixed actual heights in the
[half-index contour theorem](research_mixed_half_index_contour.md)
meet Theorem 1. No independently released \(\pm.12\) height
box is substituted here.

For that complete original source, the left tail already increases
to \(3/20\). Theorem 1 therefore gives exactly
\[
 T_*(a,b)=\max\{\mathcal R_\epsilon(3/20;a,b),
                  \mathcal R_\epsilon(1/2;a,b),
                  \mathcal R_\epsilon(1;a,b)\}.
 \tag{25}
\]
Its full finite upper bound is consequently
\(\max(B,T_*)+\tau\), with the original two supporting
marginals, quadratic loss, both Fourier halfweights, all residues and
aliases, and the single prescribed tolerance unchanged. All interior
right-tail candidates have been paid analytically. Establishing the
calibrated signs of the three rates in (25), or a specified payable
boundary excess, remains necessary. The existing restrictions on
transverse derivatives, boundary gluing, and whole open-source
dominance are not removed by this row comparison.
