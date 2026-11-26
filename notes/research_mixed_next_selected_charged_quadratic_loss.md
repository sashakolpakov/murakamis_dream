# A stronger action loss on the selected charged curve

Private written phase estimate, 9 November 2026. The selected stationary
point has depth at least \(20\pi\delta/113\). Integrating that depth
gives a quadratic loss in its original action. This improves the
previous phase estimate; it is not, by itself, an estimate for a finite
outer Fourier coefficient.

No mathematical numerical evaluation or saved-value arithmetic is used.
All inequalities below follow from the written branch bounds.

## 1. Original branch and statement

Use the selected curve and original logarithmic return from
[the full charged-curve theorem](research_mixed_next_selected_charged_curve_full_interval.md).
For \(0<\delta\le1/2\), write
\[
 u_\delta=\beta-iK,\qquad c=\cos(t_*(u_\delta)/2)=p+iq,\qquad
 w=c\tan(u_\delta/2).
\]
The adopted
[angle-depth correlation](research_mixed_next_selected_charged_angle_depth_correlation.md),
[depth bound](research_mixed_next_selected_charged_depth_bound.md),
and original selected-sheet guards give
\[
 0<\beta<8/7,\qquad
 \beta/4<K<\beta/2,\qquad K<2/5,\qquad
 3/4<p<8/9,\qquad 1/4<q<1/3.
 \tag{1}
\]
The principal inverse hyperbolic sine retains the unexponentiated
stationary equation
\[
 f=\operatorname{arsinh}w
       =\frac{3K}{2}+i\left(\frac{3\beta}{2}-\pi\delta\right).
 \tag{2}
\]
In particular \(\Re w>0\), and if \(f=X+i\nu\), then
\(-\pi/2<\nu<\pi/2\).

Let
\[
 \Psi_\delta(u)=S(u)+\frac{3iu^2}{4\pi}-i\delta u,\qquad
 \Gamma(\delta)=\Re\Psi_\delta(u_\delta),\qquad M_3=\Re S(0).
 \tag{3}
\]
These are the original calibrated actions. Their derivative identity is
\[
             M_3-\Gamma(\delta)=\int_0^\delta K_s\,ds.
 \tag{4}
\]
Here \(K_s=-\Im u_s\), and \(u_0=0\).

**Theorem.** For every \(0<\delta\le1/2\),
\[
 p>\frac{13}{16},\qquad
 K>\frac{2\beta}{7},\qquad
 K>\frac{20\pi\delta}{113}.
 \tag{5}
\]
Consequently
\[
 \Gamma(\delta)<M_3-\frac{10\pi}{113}\delta^2
                 \qquad(0<\delta\le1/2).
 \tag{6}
\]
At \(\delta=0\), the corresponding non-strict inequality is equality.
In particular
\[
                    \Gamma(1/2)<M_3-\frac{5\pi}{226}.
 \tag{7}
\]

## 2. A lower bound for the real part of the inner root

Put \(v=2c=x+ib\) and \(C=\cos(u_\delta/2)\). The original cubic is
\[
                 v^3-2iv^2-3v+2i-2C=0.
 \tag{8}
\]
Its real part gives
\[
              2\Re C=x(x^2-3b^2+4b-3).
 \tag{9}
\]
Since \(1/2<b<2/3\), the last three terms in the parentheses
are at most \(-5/3\). Also
\[
 \Re C=\cos(\beta/2)\cosh(K/2)>
           \cos(4/7)>1-\frac{8}{49}=\frac{41}{49}.
 \tag{10}
\]
Suppose \(x\le13/8\). The function \(x^3-5x/3\) is increasing
for \(x\ge3/2\), so (9) would imply
\[
 \frac{82}{49}<2\Re C
    \le x(x^2-5/3)
    \le\frac{13}{8}\left(\frac{169}{64}-\frac53\right)
    =\frac{2431}{1536}<\frac{82}{49}.
 \tag{11}
\]
The final comparison follows from
\(2431\cdot49=119119<125952=82\cdot1536\).
This contradiction gives \(x>13/8\), hence \(p>13/16\).

## 3. Improving the depth-angle comparison

Set \(D=\cos\beta+\cosh K\). The exact tangent identity gives
\[
 \Re w=\frac{p\sin\beta+q\sinh K}{D},\qquad
 \Im w=\frac{q\sin\beta-p\sinh K}{D}.
 \tag{12}
\]
Suppose \(K\le2\beta/7\). For \(0\le h\le2\beta/7\), define
\[
 F_\beta(h)=
   \frac{13\sin\beta+4\sinh h}
        {16(\cos\beta+\cosh h)}
            -\sinh(3h/2).
 \tag{13}
\]
Here \(h<16/49<1/3\). The derivative of the quotient is
\[
 \frac{4+4\cos\beta\cosh h-13\sin\beta\sinh h}
      {16(\cos\beta+\cosh h)^2}
 \le\frac{1+\cosh h}{4(1+\cos\beta)^2}<\frac12.
 \tag{14}
\]
For the strict bound, use the earlier guards
\(\cos\beta>7/30\) and \(\cosh h<8/7\), exactly as in the
angle-depth correlation proof. Thus \(F_\beta'(h)<-1\).

We show that \(F_\beta(2\beta/7)>0\). Write \(z=\beta^2\);
then \(0<z<64/49<2\). The elementary sine and hyperbolic
sine bounds give
\[
 13\sin\beta+4\sinh(2\beta/7)
     \ge\beta\left(\frac{99}{7}-\frac{13z}{6}\right),\qquad
 \sinh(3\beta/7)\le
                  \frac{3\beta/7}{1-3z/98}.
 \tag{15}
\]
The latter follows by bounding successive positive-series ratios
by the first such ratio. Likewise
\[
 \cosh(2\beta/7)
 \le1+\frac{2z/49}{1-z/147}
 \le1+\frac{294}{7139}z
 <1+\frac{z}{23}.
 \tag{16}
\]
The last comparison is \(6762<7139\). The alternating cosine
bound therefore gives
\[
          \cos\beta+\cosh(2\beta/7)
                   \le2-\frac{21z}{46}+\frac{z^2}{24}.
 \tag{17}
\]

After multiplying by the positive number \(1-3z/98\), the lower
bound for
\[
 13\sin\beta+4\sinh(2\beta/7)
 -16\sinh(3\beta/7)\{\cos\beta+\cosh(2\beta/7)\}
\]
and dividing by \(\beta>0\) is
\[
 \frac37+
 \left(\frac{504}{161}-\frac{13}{6}-\frac{297}{686}\right)z
                  -\frac{43}{196}z^2.
 \tag{18}
\]
The linear coefficient is greater than \(1/2\): subtracting
\(1/2\) gives \(224/483-297/686>0\), since
\(153664>143451\). Also \(43/196<1/4\). Thus (18) is greater than
\[
                     \frac37+\frac z2-\frac{z^2}{4}>0.
 \tag{19}
\]
This proves \(F_\beta(2\beta/7)>0\), and monotonicity in (14)
gives \(F_\beta(K)>0\).

Equations (1), (11), and (12) now imply
\[
 \Re w>
 \frac{13\sin\beta+4\sinh K}{16D}>
                                      \sinh(3K/2).
 \tag{20}
\]
But (2) and \(w=\sinh(X+i\nu)\) give
\(\Re w=\sinh(3K/2)\cos\nu\le\sinh(3K/2)\).
This contradiction proves \(K>2\beta/7\).

## 4. A signed bound on the imaginary part of the return

The elementary estimates needed here are
\[
 \sin\beta\ge\beta(1-\beta^2/6)>\frac79\beta,\qquad
 \sinh K\le\frac{K}{1-K^2/6}<\frac{75}{73}K<\frac{25}{24}K,
 \qquad D>\frac{66}{49}.
 \tag{21}
\]
For the first, \(1-64/294=115/147>7/9\). For the last,
\(\cos\beta>1-\beta^2/2>17/49\) and \(\cosh K\ge1\).
Since \(\beta>2K\), equations (1), (12), and (21) yield
\[
 \Im w>
   \frac{(1/4)(14K/9)-(8/9)(25K/24)}{D}
   =-\frac{29K}{54D}
   >-\frac{1421}{3564}K>-\frac25K.
 \tag{22}
\]
The final comparison is \(7105<7128\).

This must be transferred to the original return with the correct
sign. Write \(w=A+iB\), with \(A>0\). If \(B\ge0\), its principal
return has \(\nu\ge0\). If \(B<0\), then (12) gives
\[
 \frac{|B|}{A}<
       \frac{\sinh K}{\sin\beta}
       <\frac{25}{24}\frac{9}{7}\frac K\beta
       <\frac{75}{112}<1.
 \tag{23}
\]
On the vertical segment \(A+iy\), \(B\le y\le0\), one therefore has
\(\Re(1+(A+iy)^2)\ge1\). Its principal inverse square root has
real part at most one. Since the inverse hyperbolic sine is real
at \(A\),
\[
 \nu=-\int_B^0\Re\{1+(A+iy)^2\}^{-1/2}\,dy\ge B.
 \tag{24}
\]
Both signs of \(B\) consequently give \(\nu>-2K/5\).

Taking imaginary parts of (2), and using \( \beta<7K/2\), proves
\[
 \pi\delta=\frac{3\beta}{2}-\nu
    <\frac{21K}{4}+\frac{2K}{5}=\frac{113K}{20}.
 \tag{25}
\]
This is the final bound in (5). Integrating it in the exact
action identity (4) proves (6) and (7).

## 5. What remains separate

The improved loss is a property of the selected, correctly normalized
phase. It can enter an outer Fourier estimate only once the original
finite sum has been shown to follow that phase on its contributing
contour, with the other contributions controlled. The new inner
asymptotic along the selected curve is useful input to that step,
but a curve of inner stationary values is not itself an outer
integration cycle.

In particular (6) is not a replacement for the current whole-frequency
finite-source bound. It does not prove a lower bound for the signed
outer observation or any additional volume-conjecture case.

## Source versions

- Selected curve and calibrated action derivative:
  6828459338fff642bf52b425120ed806d39bd9847d8df5ea5db8a14f0859da0c.
- Original cubic continuation:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
- Selected sheet and lower imaginary-part guard:
  8c44e62b5015b61aa7b5a19e9706e539a6b1544be5657edb2bbc78a6ab99adfc.
- Selected upper depth and real-part guard:
  f3b0b8f8e14adb8beff461e53ec20cdcb7afb4dc07bda3e1247116b55e13c017.
- Earlier angle-depth correlation:
  49d0d81bb39dcdb8946893c8bc0b712e00b2eaad15b3f5476b62736fce1df1f4.
