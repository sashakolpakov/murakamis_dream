# A two-sided angle-depth correlation on the selected charged curve

Private phase deduction, 9 November 2026. The original selected curve
obeys \(K>\beta/4\), and consequently \(\beta<8/7\). Together with
the previously proved upper bounds, this gives a narrower actual
parameter region for the attached endpoint-sector comparison. No
finite-source or action-budget conclusion is inferred here.

No mathematical numerical evaluation, saved-value arithmetic, or
frozen-source edit is used.

## 1. Original branch and statement

Keep the original selected curve from
[the full-interval theorem](research_mixed_next_selected_charged_curve_full_interval.md)
and the actual sheet guards from
[the right-edge source-domain proof](research_mixed_next_selected_right_edge_cut_guards.md).
For \(0<\delta\le1/2\), write
\[
\begin{gathered}
u_\delta=\beta-iK,\qquad
0<\beta<4/3,\quad0<K<1/2,\quad K<\beta/2,\\
c=\cos(t_*(u_\delta)/2)=p+iq,\qquad
p>3/4,\quad1/4<q<1/3,\\
w=c\tan(u_\delta/2),\qquad
f=\operatorname{arsinh}w=X+i\nu
                   =i(3u_\delta/2-\pi\delta).
\end{gathered}
\tag{1}
\]
The inverse hyperbolic sine is the original principal logarithmic
return. In particular \(\Re w>0\), \(X>0\), and
\(-\pi/2<\nu<\pi/2\). The same sources prove
\(\cos\beta>7/30\). At \(\delta=0\), the selected value is \(u_0=0\).

**Theorem.** For every \(0<\delta\le1/2\),
\[
                 \frac{\beta}{4}<K<\frac{\beta}{2},
                 \qquad 0<\beta<\frac87 .
\tag{2}
\]
Combining this with
[the sharper depth theorem](research_mixed_next_selected_charged_depth_bound.md)
also gives \(K<2/5\). Every assertion concerns the original selected
branch, rather than all solutions of an exponentiated critical equation.

## 2. The lower depth bound

Set \(D=\cos\beta+\cosh K\). The exact tangent identity gives
\[
 \Re w=\frac{p\sin\beta+q\sinh K}{D},
 \qquad
 \Im w=\frac{q\sin\beta-p\sinh K}{D},
 \qquad D>0.
\tag{3}
\]
Suppose, for contradiction, that \(K\le\beta/4\). For
\(0\le h\le\beta/4\), put
\[
 F_\beta(h)=
 \frac{3\sin\beta+\sinh h}{4(\cos\beta+\cosh h)}
                         -\sinh(3h/2).
\tag{4}
\]
Here \(h\le1/3\). The derivative of the quotient in (4) is
\[
 \frac{1+\cos\beta\cosh h-3\sin\beta\sinh h}
           {4(\cos\beta+\cosh h)^2}
 \le \frac{1+\cosh h}{4(1+\cos\beta)^2}<\frac12.
\tag{5}
\]
For the last strict bound use \(\cos\beta>7/30\) and
\(\cosh h<8/7\). The latter follows directly from the positive
series: for \(h\le1/3\), the terms after \(h^2/2\) have successive
ratio at most \(1/108\), so
\(\cosh h\le1+6/107=113/107<8/7\).
After clearing denominators the remaining comparison in (5) is
\(13500<19166\).
It follows that \(F_\beta'(h)<-1\); therefore
\(F_\beta(K)\ge F_\beta(\beta/4)\).

We next show \(F_\beta(\beta/4)>0\). Write \(v=\beta\).
After multiplication by the positive denominator this is equivalent to
\[
 3\sin v+\sinh(v/4)>
       4\sinh(3v/8)\{\cos v+\cosh(v/4)\}.
\tag{6}
\]
The following elementary estimates hold for \(0<v\le4/3\):
\[
\begin{aligned}
3\sin v+\sinh(v/4)&\ge \frac{13v}{4}-\frac{v^3}{2},\\
\sinh(3v/8)&\le
 \frac{3v/8}{1-(3v/8)^2/6}\le\frac{9v}{23},\\
\cos v+\cosh(v/4)&\le
           2-\frac{401v^2}{856}+\frac{v^4}{24}.
\end{aligned}
\tag{7}
\]
The first and third use the alternating sine and cosine bounds.
For the hyperbolic cosine term in the third, the positive series gives
\[
\cosh(v/4)\le1+
 \frac{v^2/32}{1-v^2/192}
              \le1+\frac{27v^2}{856}.
\]
The positive hyperbolic sine terms give the second line of (7).
The left side of (6) minus its right side is consequently at least
\[
 \frac{11v}{92}+\frac{574v^3}{2461}-\frac{3v^5}{46}>0.
\tag{8}
\]
Indeed \(574/2461>1/5\), whereas
\((3/46)v^2\le8/69<1/5\). This proves (6).

Now (1),(3),(4) imply
\[
 \Re w>
 \frac{3\sin\beta+\sinh K}{4D}
 >\sinh(3K/2).
\tag{9}
\]
But the unexponentiated original equation in (1) says \(X=3K/2\),
while \(w=\sinh(X+i\nu)\) gives
\(\Re w=\sinh X\cos\nu\le\sinh(3K/2)\).
This contradicts (9), proving \(K>\beta/4\).

## 3. The resulting angle bound

If \(\Im w\le0\), the principal return has \(\nu\le0\).
Suppose instead that \(y=\Im w>0\), and put \(x=\Re w\).
Equation (3) gives
\[
                      0<\frac yx<\frac qp<\frac49.
\tag{10}
\]
On the vertical segment \(x+is\), \(0\le s\le y<x\), one has
\(\Re(1+(x+is)^2)=1+x^2-s^2\ge1\).
The principal return is holomorphic along this segment and real
at \(x\); thus
\[
\nu=\int_0^y\Re\{1+(x+is)^2\}^{-1/2}\,ds\le y.
\tag{11}
\]
Using the lower depth bound, \(p>3/4\), \(q<1/3\),
\(\sin\beta\le\beta\), \(\sinh K\ge K\), and
\(D>37/30\), the positive case yields
\[
\nu\le\Im w<
 \frac{\beta/3-3\beta/16}{37/30}
                         =\frac{35\beta}{296}.
\tag{12}
\]
The same strict upper bound is automatic when \(\nu\le0\).
Taking imaginary parts of (1) and using \(\delta\le1/2\),
\[
 \beta=\frac23(\pi\delta+\nu)
        <\frac{\pi}{3}+\frac{35\beta}{444}.
\]
Therefore
\[
 \beta<\frac{148\pi}{409}
       <\frac{3256}{2863}<\frac87 .
\tag{13}
\]
Here \(\pi<22/7\), and the last rational comparison is
\(22792<22904\).
This completes the theorem.

## 4. Scope

The proof uses the original logarithmic return before taking real and
imaginary parts. In particular, no root of a cleared polynomial has
been substituted for the selected critical point.

The narrower region (2), together with \(K<2/5\), is available for a
separate comparison of the attached endpoint sector with the original
inner action. It does not itself estimate a finite kernel, continue an
edge packet, or pay a contour.

## Frozen source bindings

- Full selected charged curve:
  6828459338fff642bf52b425120ed806d39bd9847d8df5ea5db8a14f0859da0c.
- Actual sheet and original cubic guards:
  8c44e62b5015b61aa7b5a19e9706e539a6b1544be5657edb2bbc78a6ab99adfc.
- Sharper upper depth bound:
  f3b0b8f8e14adb8beff461e53ec20cdcb7afb4dc07bda3e1247116b55e13c017.
