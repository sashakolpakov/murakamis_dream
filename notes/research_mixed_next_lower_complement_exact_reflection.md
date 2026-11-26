# Exact reflection of the complete lower next-source density

Private research deduction, 8 November 2026. Reflection exchanges
the two Fourier observations of the complete finite source. It also
changes the Newton kernel and reverses the original Fourier weight.
This note records that complete identity, including its interval
orientation and the isolated physical endpoint of the reversed weight.

The identities apply to the actual \(34\) prefix and its old
cardinal filter. They do not bound the reflected source by the
already controlled selected source. The obstruction to that direct
reuse is an exact row identity, not an action comparison or a
counterexample to suppression. No numerical evaluation or modification
of a frozen input is used.

## 1. Literal source and the two observations

Put
\[
D=N-1,\qquad r=e^{-2\pi i/N},\qquad
P_j=(r;r)_j,\qquad p_j(V)=(rV;r)_j,\qquad
f_j(V)=p_j(V)/P_j,\qquad N\ge2 .
\tag{1}
\]
All factorial indices in this note are at most \(D\).
The complete kernels and the actual prefix are
\[
\begin{split}
C_{\beta,N}(Y,Z)
 &=\sum_{j=0}^D Y^{-j}f_j(Y)f_j(Z)/P_j^\beta,
 \qquad\beta=0,1,\\
F_N(w,Y)
 &=N\operatorname{CT}_X
       [U_{0,N}(w,X)C_{1,N}(X,Y)]
   =\sum_{i=0}^D a_i(w)f_i(Y),\\
d_N(Y)&=\frac1N\sum_{\ell=0}^D f_\ell(Y),
\qquad d_N(r^b)=P_b^{-1}.
\end{split}
\tag{2}
\]
These are the literal sources of
[the next attachment](research_mixed_three_four_next_conditional_attachment.md)
and [the exact Newton quotient](research_mixed_next_selected_wrap_quotient.md),
equations (2)--(6). In particular \(a_i\) remains the coherent
coefficient of the complete first source; it is not replaced by
a positive coefficient or by a sampled asymptotic.

Let \(E_N(Y)\) be either \(F_N(w,Y)\) or its old \(11/12\)
cardinal-filtered polynomial \(F_N^{\rm mid}(w,Y)\). Define
\[
A_N(Y,Z)=E_N(Y)d_N(Y)C_{\beta,N}(Y,Z).
\tag{3}
\]
Then
\[
\operatorname{band}_Y A_N\subset[-D,2D].
\tag{4}
\]
The original two observations, with their original outside level
factor, are
\[
S_0[E_N]=N[Y^0]A_N,\qquad S_1[E_N]=N[Y^N]A_N .
\tag{5}
\]
They obey the exact full-source identity
\[
S_0[E_N]+S_1[E_N]
=\sum_{b=0}^D E_N(r^b)P_b^{-1}C_{\beta,N}(r^b,Z).
\tag{6}
\]
This is [cardinal-sector separation, Section 1](research_mixed_next_cardinal_sector_separation.md).
Every physical row, including both true endpoints, is retained.

## 2. Reflect the kernel before estimating it

For a polynomial \(f\), write \(f^{\rm c}(V)=\overline{f(\bar V)}\).
Factorwise conjugation gives the exact identity
\[
\overline{P_j}=(-1)^j r^{-j(j+1)/2}P_j,\qquad
f_j^{\rm c}(V)=V^j f_j(V^{-1}).
\tag{7}
\]
The right side of the second identity is a polynomial, including
its value at zero. Thus inversion of the original incoming
kernel gives
\[
\boxed{\quad
C_{\beta,N}(V^{-1},Z)
=\sum_{j=0}^D f_j^{\rm c}(V)f_j(Z)/P_j^\beta .
\quad}
\tag{8}
\]
The factor \(V^j\) in the original incoming carrier cancels the
factor \(V^{-j}\) from (7). In particular (8) is a polynomial
in \(V\), rather than the original Laurent kernel with band
\([-D,0]\).

There is an equivalent exact complementary-index formula:
\[
p_D(V)=\frac{1-V^N}{1-V},\qquad
P_j\overline{P_{D-j}}=N,\qquad
f_j^{\rm c}(V)=\frac{p_D(V)}{Nf_{D-j}(V)} .
\tag{9}
\]
At zeros of the displayed denominator the quotient means its
polynomial continuation. To prove the last identity, the quotient
\(p_D/p_{D-j}\) is precisely
\(\prod_{k=1}^j(1-r^{-k}V)\), and
\(P_{D-j}/N=1/\overline{P_j}\).
Consequently
\[
C_{\beta,N}(V^{-1},Z)
=\frac{p_D(V)}N
  \sum_{j=0}^D\frac{f_j(Z)}{P_j^\beta f_{D-j}(V)} .
\tag{10}
\]
Equation (10) does not license deletion of any term at a root
of a denominator. It is an identity of the complete canceled
rational expressions. It keeps both \(j=0\) and \(j=D\).

There is no scalar correction of the incoming variable that
turns (8) into the old kernel on an open set. More precisely,
if
\[
C_{\beta,N}(V^{-1},Z)=m(V)C_{\beta,N}(V,Z)
\tag{11}
\]
holds for all \(Z\), the independent Newton basis \(f_j(Z)\)
first gives \(m(V)=1\) from \(j=0\). The \(j=1\) coefficient
then requires
\[
\frac{V-r}{1-r}
  =f_1^{\rm c}(V)
  =V^{-1}f_1(V)=\frac{V^{-1}-r}{1-r},
\]
hence \(V^2=1\). Therefore (11) cannot hold on any open
complex domain. The same test applies after multiplying the
kernel by nonzero scalar prefix and Fourier factors: they
cannot remove its row-dependent change.

This statement excludes direct scalar reuse of the old kernel
estimate. It does not exclude a new estimate for (8), a
non-scalar change of basis, or cancellation in the full source.

## 3. The reversed weight retains its isolated endpoint and forcing

Reverse only the degree-\(D\) polynomials:
\[
E_N^\sharp(V)=V^D E_N(V^{-1}),\qquad
d_N^\sharp(V)=V^D d_N(V^{-1}).
\tag{12}
\]
They are polynomials of degree at most \(D\). At physical nodes
the second one has the exact values
\[
\boxed{\quad
d_N^\sharp(1)=1,\qquad
d_N^\sharp(r^b)=\frac{r^{-b}\overline{P_{b-1}}}{N}
=\frac{\overline{P_b}}{N(r^b-1)}
\quad(1\le b\le D).
\quad}
\tag{13}
\]
Indeed \(P_{N-b}\overline{P_{b-1}}=N\) and
\((r^b)^D=r^{-b}\). The formula for \(b\ge1\) has no
value at \(b=0\); the separate value one in (13) is mandatory.
These are conjugate factorial values, not the old inverse
factorial values \(P_b^{-1}\).

The complete original forced equation is
\[
d_N(r^{-1}Y)=(1-Y)d_N(Y)
                 +\frac{Y}{N^2}\sum_{k=0}^D Y^k ,
\tag{14}
\]
as in [Fourier-weight continuation, equation (5)](research_mixed_fourier_weight_continuation.md).
Substitution of \(Y=V^{-1}\) gives
\[
\boxed{\quad
rVd_N^\sharp(rV)
=(V-1)d_N^\sharp(V)+\frac1{N^2}\sum_{k=0}^D V^k .
\quad}
\tag{15}
\]
In particular \(d_N^\sharp(0)=N^{-2}\), the original top
coefficient of \(d_N\). There is no nonzero polynomial
solution of the homogeneous equation obtained by deleting the
last term of (15). For if \(h(V)=\sum h_kV^k\) satisfies it,
its constant coefficient is \(h_0=0\), and successive
coefficients give
\(h_k=(1-r^k)h_{k-1}=0\).
Thus discarding the forcing would discard the entire polynomial
weight, not just a smaller endpoint term.

One can also isolate the endpoint in an exact interpolation
identity. Let \(e_N(V)\) be the degree-\(D\) polynomial with
\(e_N(r^b)=\overline{P_b}\), and put
\(\mathfrak l_0(V)=N^{-1}\sum_{k=0}^D V^k\).
Then
\[
\boxed{\quad
(V-1)d_N^\sharp(V)
=\frac{e_N(V)-\mathfrak l_0(V)}N
                   +d_N(0)(V^N-1).
\quad}
\tag{16}
\]
Both sides agree at every physical node by (13). Their
difference has degree at most \(N\), and the coefficient of
\(V^N\) on the left is \(d_N(0)\), proving the formula.
Neither \(\mathfrak l_0\) nor the term proportional to
\(V^N-1\) may be dropped when inserting (16) into a contour
density. No bound on the new factorial interpolant \(e_N\)
is assumed here.

## 4. The full source and its shifted Fourier observations

Define the reversed Laurent kernel and the reversed full source by
\[
C_{\beta,N}^{\leftarrow}(V,Z)
      =V^{-D}C_{\beta,N}(V^{-1},Z),\qquad
A_N^\dagger(V,Z)
      =E_N^\sharp(V)d_N^\sharp(V)
                           C_{\beta,N}^{\leftarrow}(V,Z).
\tag{17}
\]
Then exactly
\[
A_N^\dagger(V,Z)=V^D A_N(V^{-1},Z),\qquad
\operatorname{band}_V A_N^\dagger\subset[-D,2D].
\tag{18}
\]
The \(E^\sharp,d^\sharp\) in (17) are polynomials; the
complete \(A^\dagger\) is generally a Laurent polynomial.
The original observations become
\[
\boxed{\quad
S_0[E_N]=N[V^D]A_N^\dagger,\qquad
S_1[E_N]=N[V^{-1}]A_N^\dagger .
\quad}
\tag{19}
\]
Thus degree reversal by \(D=N-1\) does not by itself give
the original coefficient labels \(0,N\).

An additional single factor of \(V\) records the exact sector
exchange:
\[
\widehat A_N(V,Z):=V A_N^\dagger(V,Z)
                  =V^N A_N(V^{-1},Z).
\tag{20}
\]
Its band is contained in \([1-D,2D+1]\), whose only
multiples of \(N\) are still \(0,N\). Hence
\[
\boxed{\quad
S_0[E_N]=N[V^N]\widehat A_N,\qquad
S_1[E_N]=N[V^0]\widehat A_N .
\quad}
\tag{21}
\]
Root averaging consequently preserves their sum:
\[
\sum_{V^N=1}\widehat A_N(V,Z)
=\sum_{Y^N=1}A_N(Y,Z).
\tag{22}
\]
Equations (20)--(22) exchange the Fourier sectors of the
transformed full source. They do not identify \(\widehat A_N\)
with the original prefix/weight/kernel product at \(V\).

For the old cardinal filter, reflection also reverses its
physical support:
\[
E_N^\sharp(r^b)=r^{-b}E_N(r^{-b}).
\tag{23}
\]
In particular a deleted physical set becomes its inverse set.
It is not replaced by the old low/high deletion range. The
finite values and all their cancellations are retained by (23).

## 5. Interval orientation and the paired meromorphic density

Use the actual logarithmic variable
\(Y=e^{-2\pi iy}\), and let a reflected coordinate be
\(\zeta=1-y\), so \(V=e^{-2\pi i\zeta}=Y^{-1}\).
For any \(0\le a<b\le1\) and \(h<0\), reflection maps
\([a,b]+ih\) to \([1-b,1-a]-ih\) after reversing its
parametrization. The literal unselected and selected densities
satisfy respectively
\[
\begin{split}
N\int_{a+ih}^{b+ih}A_N(Y,Z)\,dy
 &=N\int_{1-b-ih}^{1-a-ih}
                    V^{-N}\widehat A_N(V,Z)\,d\zeta,\\
N\int_{a+ih}^{b+ih}Y^{-N}A_N(Y,Z)\,dy
 &=N\int_{1-b-ih}^{1-a-ih}
                             \widehat A_N(V,Z)\,d\zeta .
\end{split}
\tag{24}
\]
There is no extra factor \(N\), root phase, or change of the
outgoing variable \(Z\) in these formulas.

For the old filtered source the exact cyclic contour uses
\[
K_N(y,Z)=\frac{N A_N(Y,Z)}{1-Y^N},
\qquad
\widehat K_N(\zeta,Z)
               =\frac{N\widehat A_N(V,Z)}{1-V^N}.
\tag{25}
\]
These are the densities of
[the paired cyclic reduction](research_mixed_next_paired_cyclic_horizontal_reduction.md).
The full finite identity is
\[
K_N(y,Z)=-\widehat K_N(1-y,Z),
\]
and hence
\[
\boxed{\quad
\int_{a+ih}^{b+ih}K_N(y,Z)\,dy
=-\int_{1-b-ih}^{1-a-ih}
                         \widehat K_N(\zeta,Z)\,d\zeta .
\quad}
\tag{26}
\]
In particular the still-missing lower right interval
\([1/2,1]+ih_y\) becomes the negative upper interval
\([0,1/2]-ih_y\) for this transformed density. Its height is
the actual \(-h_y\), with no replacement by \(1/100\).
The numerator is the entire transformed product (17),(20),
not the old selected numerator.

If both lower and upper parts of a paired cycle are reflected,
(26) exchanges them with their original opposite signs. Thus
reflection preserves the exact paired identity, rather than
eliminating one of its sectors or one of its complementary
currents. Deleted physical poles remain removable by (23);
retained physical poles remain retained.

## 6. Adjoint reflection is a different operation

A simultaneous conjugate reciprocal reflection and exchange
of the two kernel arguments gives
\[
\begin{split}
\overline{C_{\beta,N}(1/\bar Z,1/\bar Y)}
 &=\sum_{j=0}^D
 \frac{Y^{-j}f_j(Y)f_j(Z)}{\overline{P_j}^{\,\beta}}\\
 &=\sum_{j=0}^D
 \tau_j^\beta\frac{Y^{-j}f_j(Y)f_j(Z)}{P_j^\beta},
\qquad \tau_j=(-1)^j r^{j(j+1)/2}.
\end{split}
\tag{27}
\]
For \(\beta=0\) this is the original Gram symmetry. It
changes both arguments, and is not the one-variable reflection
(8). For type four it retains the explicit diagonal row
phase \(\tau_j\). When \(N\ge3\), already
\(\tau_1=-r\ne1\), so the type-four kernel does not obey the
same adjoint symmetry. The \(N=2\) exceptional phase causes
no exception to the finite identities above.

The actual \(34\) prefix in (2) itself contains this type-four
kernel. Even when the following kernel has \(\beta=0\),
its adjoint symmetry alone therefore does not reflect the
entire incoming source into itself. The corresponding
coefficient-space identity in
[the selected Gram response, Section 2](research_mixed_next_selected_response_gram_structure.md)
retains a distinct adjoint observation and the full original
forcing polynomial; it does not identify that observation
with a conjugate response at a general complex output.

The precise new source left by reflection is (17),(20), or
equivalently the complementary-index expression (10) coupled
to (12),(15). A bound for its selected upper integral would
bound the original lower right integral by (24) or (26).
The old selected theorem supplies no such bound solely by
scalar normalization: (11), the reversed weight (13)--(16),
and the changed physical filter (23) are exact finite
differences that must be controlled together.

All statements are identities of the original finite
polynomials or their displayed Laurent and meromorphic
densities. They hold for both parities, arbitrary ordinary
color, and every fixed ordinary/output derivative. No
asymptotic continuation, action comparison, or suppression
of the remaining interval is claimed.

