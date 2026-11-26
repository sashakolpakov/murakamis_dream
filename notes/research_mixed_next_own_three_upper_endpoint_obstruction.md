# An obstruction to an endpoint-only own-three upper-row bound

Private research deduction, 8 November 2026. The complete positive
own-three upper block cannot, on the enlarged independent height box
alone, be reduced to its half-row and last-row rates. An exact
original-row example has an interior upper row strictly above both
endpoints. This distinguishes the remaining own-three problem from
the proved own-four reduction.

The example does **not** assert that these independent parameters
are realized by an actual ordinary-next geometric reference. It is
not a counterexample to the required joint supporting-plane bound,
or to a coherent bound for the full conditional kernel. No numerical
evaluation or modification of a frozen source is used.

## 1. Literal source and a permitted point of the containing box

Keep the original next own-three source
\[
C_{0,N}(Y,Z)=\sum_{j<N}
 \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2},
\qquad
Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz}.
\tag{1}
\]
Its physical rate, including the incoming carrier, is
\[
E_0(t;y,z)=
\int_0^t\log|1-e^{-2\pi i(y+s)}|\,ds+
\int_0^t\log|1-e^{-2\pi i(z+s)}|\,ds
-2J(t)-2\pi t\Im y .
\tag{2}
\]
Use the exact reflected formula from
[right-tail reflection, equations (3)--(4)](research_mixed_right_tail_reflection.md).
Set
\[
y=-\,\frac{i}{2\pi}\log\frac53,\qquad z=\frac{11}{50},
\qquad T=\frac53 .
\tag{3}
\]
Thus \(q=\Re y=0\), \(\Re z\in P=[11/50,9/20]\),
and \(\Im z=0\). Moreover
\[
\frac12<\log\frac53<\frac{13}{25},
\qquad
-\frac{52}{625}<\Im y<-\frac7{88}.
\tag{4}
\]
The lower logarithm bound is
\(2\operatorname{arctanh}(1/4)>1/2\).
For the upper bound,
\[
e^{13/25}>
1+\frac{13}{25}+\frac{(13/25)^2}{2}
 +\frac{(13/25)^3}{6}
=\frac{157372}{93750}>\frac53 .
\]
The height bounds in (4) follow from \(25/8<\pi<22/7\).
They lie strictly inside the printed ordinary-next containing
bounds \(-.102<\Im y<-.001\), \(|\Im z|\le.108\).
No assertion about the actual reference image is made.

Define the reflected rate difference
\[
\Phi(v)=E_0(1-v;y,z)-E_0(1;y,z),\qquad 0\le v\le\frac12.
\]
The full-period mean and original carrier give
\[
\begin{split}
E_0(1;y,z)&=\log T,\\
\Phi(v)&=2J(v)
-\int_0^v\log|T-e^{2\pi is}|\,ds
-\int_0^v\log|1-e^{-2\pi i(11/50-s)}|\,ds .
\end{split}
\tag{5}
\]
The second integral may have its integrable zero; it is not
deleted or replaced by a different Fourier branch.

## 2. The half-row is above the last row but slopes toward a larger row

Evenness and the full-period logarithmic mean give
\[
\int_0^{1/2}\log|T-e^{2\pi is}|\,ds=\frac12\log T.
\]
The second integral in (5) is
\(J(11/50)+J(7/25)\). Since \(J(1/2)=0\),
\[
\Phi(1/2)
=-\frac12\log\frac53-J(11/50)-J(7/25).
\tag{6}
\]
The elementary Catalan witness in
[the half-interval packet, equation (21)](research_repeated_two_block_half_interval_packet.md)
gives \(-J(1/4)>63/440\).
Also \(J'>0\) between \(11/50\) and \(1/4\), whereas
\(J'(s)<\log2<7/10\) between \(1/4\) and \(7/25\).
Consequently
\[
\begin{split}
-J(11/50)-J(7/25)
&>\frac{63}{220}-\frac{21}{1000}
 =\frac{2919}{11000},\\
\Phi(1/2)&>
\frac{2919}{11000}-\frac{13}{50}
=\frac{59}{11000}>0 .
\end{split}
\tag{7}
\]
Thus the half-row strictly exceeds the last-row rate.

On the other hand, differentiating the literal reflected
formula at \(v=1/2\) gives
\[
\exp\Phi'(1/2)=
\frac{4}{(T+1)\sqrt{2+2\cos(11\pi/25)}}
=\frac{3}{2\sqrt{2+2\cos(11\pi/25)}}<1.
\tag{8}
\]
Indeed
\[
\cos(11\pi/25)=\sin(3\pi/50)
>\sin(3/16)>\frac3{16}-\frac{(3/16)^3}{6}>\frac18.
\]
This makes the denominator squared in the last expression
of (8) strictly greater than nine. Hence \(\Phi'(1/2)<0\).
All factors are nonzero near that endpoint, so the derivative
is continuous there. There is therefore a \(v_0<1/2\),
arbitrarily close to \(1/2\), with
\[
\Phi(v_0)>\Phi(1/2)>0 .
\]
Equivalently, for \(t_0=1-v_0>1/2\),
\[
\boxed{\quad
E_0(t_0;y,z)>
\max\{E_0(1/2;y,z),E_0(1;y,z)\}.
\quad}
\tag{9}
\]
The choice can be made with \(t_0<3/5\). In particular
the outgoing products at these rows have not reached their
first zero at continuum index \(1-11/50\).

## 3. Finite consequence and the precise limitation

Fix such a \(t_0\), and let \(j_N=\lfloor Nt_0\rfloor\).
The original uniform sine-factorial estimate and the regular
numerator product estimates give
\[
\log\left|
\frac{Y^{-j_N}p_{j_N}(Y)p_{j_N}(Z)}{P_{j_N}^2}
\right|
=NE_0(t_0;y,z)+O(\log N).
\tag{10}
\]
There is no numerator zero in these products: \(Y=3/5\)
is strictly inside the disk, and all outgoing arguments stay
strictly between \(11/50\) and \(11/50+3/5<1\).
The finite statement includes both parities.

Thus, for some fixed \(\gamma>0\), all sufficiently large \(N\)
satisfy
\[
\sum_{\lceil N/2\rceil\le j<N}
\left|\frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}\right|
>
\exp N\left[
\max\{E_0(1/2;y,z),E_0(1;y,z)\}+\gamma
\right].
\tag{11}
\]
Any row-independent allocation cancels in this comparison.
The positive upper block therefore has no endpoint-only
bound with arbitrarily small exponential tolerance on the
whole independent box containing (3).

The actual geometric heights and closing observations remain
correlated. Equation (11) neither places (3) in that reference
image nor gives a lower bound for the coherent sum (1).
The remaining actual problem may still be resolved by those
correlations, by a joint comparison with the first factor,
or by a full coherent upper-row argument. The own-four
theorem and all already paid lower-half currents are unchanged.
