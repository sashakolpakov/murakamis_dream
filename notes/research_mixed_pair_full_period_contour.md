# An exact full-period contour for the mixed two-crossing source

The mixed source has selected heights of opposite signs. Its exact
residue formula can use the upper horizontal contour in the first
variable and the lower horizontal contour in the second. Extending
the first index through its entire original range removes the
diagonal staircase. The two vertical sides then combine by an exact
translation identity.

This note proves the resulting finite contour identity and states
all of its remaining estimates explicitly. It does not discard a
Fourier correction or an endpoint current on the basis of the
horizontal maximum alone.

## 1. The exact rectangular source

Use the original factorial interpolation from the
[mixed-source calculation](research_mixed_two_crossing_horizontal_dominance.md):
\[
 \begin{split}
 f_N(x,y;u)={}&N^2
    \exp\{i\pi N(xy-y^2/2-y/2)+i\pi y/2\}\\
 &\qquad\times
   \frac{G_N(N(x+y))}{G_N(Nx)^3G_N(Ny)^2}B_N(y,u).
 \end{split}                                                    \tag{1}
\]
Here \(u\) is the original free boundary angle, and \(B_N\)
interpolates the original Newton polynomial:
\(B_N(j/N,u)=e_j(-2\cos u)\). Its midpoint shifts remain
\((N-1)/2\). The source includes all the original normal data.

Fix \(\epsilon=10^{-6}\) and define
\[
 L_N=\lceil\epsilon N\rceil,\quad
 R_N=\lfloor(1/2-\epsilon)N\rfloor,
 \quad
 a_N=-\frac1{2N},\quad b_N=1-\frac1{2N},
\]
\[
 c_N=\frac{L_N-1/2}{N},\qquad d_N=\frac{R_N+1/2}{N}.
                                                               \tag{2}
\]
Only \(N\) large enough that this retained interval is nonempty
is needed. The finitely many smaller levels are irrelevant to an
asymptotic assertion. Let \(I_N=[a_N,b_N]\) and
\(J_N=[c_N,d_N]\). The retained source is exactly
\[
 Z_N^{\rm ret}(u)=
       \sum_{i=0}^{N-1}\sum_{j=L_N}^{R_N}f_N(i/N,j/N;u).
                                                               \tag{3}
\]
Indeed \(G_N(i+j)=0\) when \(N\le i+j\le2N-2\), while
all denominator indices at these lattice points remain below \(N\).
Thus extending the triangular sum to (3) adds zero terms, including
all their derivatives in \(u\). The omitted \(j\)-sectors are
part of the proved original-index tail; their real-boundary rate is
at most \(19/25\).

The divisor proof and Corollary 3a of the
[rectangular-extension note](research_adjacent_pair_rectangular_extension.md)
apply to (1) without change: the two sources differ only by a
nowhere-zero entire exponential. They prove holomorphy on a
neighborhood of every finite-height rectangle used below. This
includes every real boundary angle and a sufficiently small complex
strip. Apparent poles in reciprocal factorials are interpreted by
their removable continuation.

Let \((x_*,y_*)\) be the cubic critical point in the mixed-source
calculation, and put
\[
 H=\Im x_*>0,\qquad K=-\Im y_*>0.
                                                               \tag{4}
\]
The certified enclosures give
\(H=0.0629446436\ldots\) and \(K=0.0787674574\ldots\).
The first rectangle has heights \(\pm H\), and the second
has heights \(\pm K\). These heights are fixed before \(N\)
tends to infinity.

## 2. Upper and lower versions of the residue formula

For an interval \([a,b]\) with half-grid endpoints and a
holomorphic function \(F\), the upper-base residue identity is
\[
 \begin{split}
 \sum_{a<k/N<b}F(k/N)
 ={}&N\int_a^b\frac{F(x+ih)}{1-e^{2\pi iN(x+ih)}}\,dx\\
 &+N\int_a^b F(x-ih)
       \frac{e^{-2\pi iN(x-ih)}}{1-e^{-2\pi iN(x-ih)}}\,dx\\
 &-iN\int_{-h}^{h}
       \frac{F(b+is)-F(a+is)}{1+e^{-2\pi Ns}}\,ds.
 \end{split}                                                   \tag{5}
\]
The lower-base identity is
\[
 \begin{split}
 \sum_{a<k/N<b}F(k/N)
 ={}&N\int_a^b\frac{F(y-ik)}{1-e^{-2\pi iN(y-ik)}}\,dy\\
 &+N\int_a^b F(y+ik)
       \frac{e^{2\pi iN(y+ik)}}{1-e^{2\pi iN(y+ik)}}\,dy\\
 &+iN\int_{-k}^{k}
       \frac{F(b+it)-F(a+it)}{1+e^{2\pi Nt}}\,dt.
 \end{split}                                                   \tag{6}
\]
The signs of the two endpoint terms are different. To prove (5),
integrate \(NF(z)/(e^{2\pi iNz}-1)\) counterclockwise around
the rectangle. Its residues are \(F(k/N)/(2\pi i)\).
For (6), use \(NF(z)e^{2\pi iNz}/(e^{2\pi iNz}-1)\)
instead. At a half-grid endpoint the exponential is
\(-e^{-2\pi Ns}\); orienting the two vertical sides gives
exactly the endpoint kernels in (5) and (6).

Each principal horizontal denominator is the sum of the constant
kernel and its complete Fourier correction. Keeping it intact
combines the usual four-term identity into three terms. No mode
has been dropped.

## 3. The mixed translation multiplier

The exact factorial relation
\(G_N(z+N)=-2\sin(\pi z)G_N(z)\) gives
\[
 f_N(x+1,y;u)=\mathcal R_N(x,y)f_N(x,y;u),
 \qquad
 \mathcal R_N(x,y)
   =-\frac{P(PV-1)}{(P-1)^3},
\]
\[
 P=e^{2\pi iNx},\qquad V=e^{2\pi iNy}.
                                                               \tag{7}
\]
The entire exponential in (1) supplies \(e^{i\pi Ny}\)
under this translation. Together with the sine-factor ratio, it
gives precisely (7).

On the left side \(x=a_N+is\), set \(T=e^{2\pi Ns}\).
Then \(P=-T^{-1}\) at every integer level, and
\[
 \mathcal R_N(a_N+is,y)=\frac{T(V+T)}{(1+T)^3}.
                                                               \tag{8}
\]
Combining the two vertical sides of (5) therefore gives
\[
 -iN\int_{-H}^{H}D_N(s,y)f_N(a_N+is,y;u)\,ds,
\]
\[
 \boxed{\displaystyle
 D_N(s,y)=\frac{T[TV-1-3T-2T^2-T^3]}{(1+T)^4}.}
                                                               \tag{9}
\]
These are meromorphic identities before restriction and holomorphic
identities on the stated sides. In particular \(V\) must remain
\(e^{2\pi iNy}\) on the later complex \(y\)-contours. Its value
one on the integer grid does not permit replacing it there.

## 4. The complete nine-term identity

For the two horizontal \(x\)-contours define
\[
 k_+(z)=\frac1{1-e^{2\pi iNz}},\qquad
 k_-(z)=\frac{e^{-2\pi iNz}}{1-e^{-2\pi iNz}}.
\]
For the lower and upper \(y\)-contours define
\[
 \ell_-(z)=\frac1{1-e^{-2\pi iNz}},\qquad
 \ell_+(z)=\frac{e^{2\pi iNz}}{1-e^{2\pi iNz}},\qquad
 w_N(t)=\frac1{1+e^{2\pi Nt}}.
                                                               \tag{10}
\]
Write \(\Delta_y F=F(d_N+it)-F(c_N+it)\) when the imaginary
coordinate is \(t\). For \(\sigma,\tau\in\{+,-\}\), put
\[
 \mathcal H_{\sigma\tau}
   =N^2\int_{I_N}\int_{J_N}
       k_\sigma(x+\sigma iH)\ell_\tau(y+\tau iK)
       f_N(x+\sigma iH,y+\tau iK;u)\,dy\,dx.
                                                               \tag{11}
\]
Here a sign in an argument means the numerical sign \(\pm1\).
There are two uncombined \(y\)-endpoint terms,
\[
 \mathcal V_\sigma
   =iN^2\int_{I_N}\int_{-K}^{K}
      k_\sigma(x+\sigma iH)w_N(t)
      \Delta_y f_N(x+\sigma iH,\cdot;u)\,dt\,dx,
                                                               \tag{12}
\]
and two combined \(x\)-side terms,
\[
 \mathcal S_\tau
   =-iN^2\int_{-H}^{H}\int_{J_N}
      \ell_\tau(y+\tau iK)D_N(s,y+\tau iK)
      f_N(a_N+is,y+\tau iK;u)\,dy\,ds.
                                                               \tag{13}
\]
Finally the combined corner term is
\[
 \mathcal C=N^2\int_{-H}^{H}\int_{-K}^{K}w_N(t)
    \Delta_y\left[D_N(s,\cdot)
                       f_N(a_N+is,\cdot;u)\right]dt\,ds.
                                                               \tag{14}
\]
The plus sign in (14) is \((-i)(i)\), from the two endpoint
identities.

**Exact contour identity.** At every sufficiently large integer
level, and for all boundary parameters for which the displayed
expressions are continued holomorphically,
\[
 \boxed{\displaystyle
 Z_N^{\rm ret}
   =\sum_{\sigma,\tau\in\{+,-\}}\mathcal H_{\sigma\tau}
     +\mathcal V_++\mathcal V_-
     +\mathcal S_++\mathcal S_-+\mathcal C.}
                                                               \tag{15}
\]

First apply (5) in \(x\) to each original \(j\), combine its
two sides by (9), and then apply (6) in \(y\) at every fixed
point of each integral. This proves (15) by substitution. For the
combined term, (6) is applied to the entire product \(D_Nf_N\).
All integrations are over fixed compact sets, so exchanging these
finite iterated integrals is legitimate. Expanding \(k_+\) and
\(\ell_-\) into their constant and correction parts recovers all
sixteen terms of the uncombined formulation. There are no diagonal
or staircase currents.

## 5. Exact kernel bounds and the surfaces to estimate

For \(s,t\in\mathbb R\), define the piecewise linear function
\[
 E(s,t)=
 \begin{cases}
 \max\{0,-4\pi s-2\pi t\},&s\ge0,\\
 \max\{2\pi s,4\pi s-2\pi t\},&s\le0.
 \end{cases}                                                   \tag{16}
\]
Both definitions agree at \(s=0\). Since
\(|e^{2\pi iNy}|=e^{-2\pi N\Im y}\), (9) proves the exact
bound
\[
                    |D_N(s,y)|\le8e^{NE(s,\Im y)}.
                                                               \tag{17}
\]
For \(T\ge1\), divide the numerator by \(T^4\); the five
terms are bounded by \(T^{-2}|V|,1,3,2,1\). For
\(T\le1\), they are bounded by \(T^2|V|,T,3T,2T,T\).
These give (17) in the two cases. Also
\[
 0<w_N(t)\le e^{-2\pi N(t)_+},\qquad (t)_+=\max(t,0).
                                                               \tag{18}
\]
For large \(N\), the horizontal kernels have absolute bounds
\(2\) for \(k_+,\ell_-\),
\(2e^{-2\pi NH}\) for \(k_-\), and
\(2e^{-2\pi NK}\) for \(\ell_+\).

The real source rate at complete boundary, on the indicated
continued branches, is
\[
 \begin{split}
 \mathcal F(a,b;s,t)={}&\Re J(a+b+i(s+t))-3\Re J(a+is)\\
 &-6\Re J(b+it)+\Re J(2b+2it)\\
 &-\pi\{bs+(a-b-1/2)t\}.
 \end{split}                                                   \tag{19}
\]
At zero height the real part of \(J\) is its continuous boundary
value. The upper and lower continuations have the same real boundary
value, including beyond the real argument one. Bounds for the exact
factorial at zero height still require the uniform endpoint estimate;
they are not a consequence of the half-plane asymptotic alone.

The following table specifies all nonprincipal estimates at limiting
real endpoints. Actual endpoints are those in (2).

| Term | Domain | Rate to bound |
|---|---|---|
| \(\mathcal H_{++}\) | \(0\le a\le1,\ 0\le b\le1/2\) | \(\mathcal F(a,b;H,K)-2\pi K\) |
| \(\mathcal H_{--}\) | same rectangle | \(\mathcal F(a,b;-H,-K)-2\pi H\) |
| \(\mathcal H_{-+}\) | same rectangle | \(\mathcal F(a,b;-H,K)-2\pi(H+K)\) |
| \(\mathcal V_+\) | \(0\le a\le1,\ -K\le t\le K,\ b=0,1/2\) | \(\mathcal F(a,b;H,t)-2\pi(t)_+\) |
| \(\mathcal V_-\) | same domain | \(\mathcal F(a,b;-H,t)-2\pi H-2\pi(t)_+\) |
| \(\mathcal S_-\) | \(-H\le s\le H,\ 0\le b\le1/2\) | \(\mathcal F(0,b;s,-K)+E(s,-K)\) |
| \(\mathcal S_+\) | same domain | \(\mathcal F(0,b;s,K)+E(s,K)-2\pi K\) |
| \(\mathcal C\) | \(-H\le s\le H,\ -K\le t\le K,\ b=0,1/2\) | \(\mathcal F(0,b;s,t)+E(s,t)-2\pi(t)_+\) |

This table is an exact account of the exponential factors in the
rational kernels. To use it for an asymptotic theorem, each listed
rate needs a strict bound below the selected action, with a
quantified allowance for \(\epsilon\), the half-grid shifts,
and a small boundary-parameter neighborhood. It does not assert
those eight bounds.

## 6. The principal term is the known horizontal integral

The principal term is \(\mathcal H_{+-}\). On its fixed heights,
\[
 k_+(x+iH)\ell_-(y-iK)
       =1+O(e^{-2\pi NH}+e^{-2\pi NK})
                                                               \tag{20}
\]
uniformly in the real coordinates. The
[half-plane factorial continuation lemma](research_factorial_uniform_halfplane_continuation.md)
applies to both signs of height. In particular \(x+y\) has
height \(H-K<0\), separated from zero, even where
\(\Re(x+y)>1\). It gives the continued asymptotic (7) of the
mixed-source note on the entire rectangular principal contour,
with its same normalization and square-root branches. Its
half-grid endpoints are also covered by the same fixed compact
half-plane sets. The shifted Newton factors use their original
bulk or midpoint formulas.

The certified horizontal maximum therefore proves that the integral
with the two kernels replaced by one has the same nonzero local
Gaussian coefficient as equation (16) of that note. The region
added beyond its compact polygon avoids the critical point and
has a strict gap. Formula (20) shows that keeping the kernels
does not change this leading coefficient. This statement persists
on a sufficiently small complex disk in \(u\).

Thus the principal term of the exact identity is established. The
eight surface bounds in the table, including their finite-level
factorial control, are proved in the companion
[contour-face estimates](research_mixed_pair_contour_face_bounds.md).
They bound every nonprincipal term by a polynomial times
\(e^{113N/100}\), uniformly at complete boundary, and retain a
strict gap on a small complex boundary disk. The exact identity
itself introduces no new invariant, no discarded normal derivative,
and no unlisted contour current.
