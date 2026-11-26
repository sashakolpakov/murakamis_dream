# Positive self-adjoint norms lose the required outer cancellation

Private exact-source deduction, 8 November 2026. The shortened
Askey--Wilson transport does have a positive self-adjoint realization
after the original outer annihilator is imposed. Every such realization,
however, is diagonal in the physical-node basis. Its Cauchy--Schwarz
bound for the actual source is already too large at the constant mode.
This conclusion holds for all choices of positive weights, including
weights depending on the level and on the source.

The failed bound is a positive norm bound, not the original signed
outer observation. No lower bound for that signed observation or for
the remaining transfer is asserted. No mathematical numerical
evaluation or frozen-source edit is used.

## 1. The exact reduced operator

Keep
\[
 N\ge3,\quad D=N-1,\quad m=\lfloor N/2\rfloor,\quad
 M=\lceil N/2\rceil,\quad U=m-1,\quad
 c_j=2\cos((2j+1)\pi/N),
                                                                    \tag{1}
\]
and the original Newton polynomials, crossing \(R_N\), and full
Hermite trace \(\phi_N\). Write
\[
 \mathscr P_N(w)=2T_N(w/2)+2,\qquad
 r_N(w)=\prod_{j=0}^{U}(w-c_j),\qquad
 \mathcal A_N=\mathbb C[w]/(\mathscr P_N).
                                                                    \tag{2}
\]
The exact shortened turn and crossed map are
\[
\begin{split}
 (\mathscr S_U f)(w)
   &=\phi_N^{(z)}
       [f(z)K_N^{<,\mathrm{ord}}(z,w)],\\
 \mathsf F_Nf&=\mathscr S_U(R_N^3f),\qquad
 \mathcal B_N=\{p\in\mathbb C[w]:\deg p\le U\}.
\end{split}                                                       \tag{3}
\]
All objects are those of the
[short-kernel operator transport](research_mixed_next_short_kernel_outer_operator_transport.md).
In particular the complete inner normals are present in (3).

The map \(\mathsf F_N:\mathcal A_N\to\mathcal B_N\) is surjective.
Indeed the original pairing
\(\phi_N(e_i e_j)=\mathbf1_{i+j=D}\) gives
\[
             \mathsf F_N(R_N^{-3}e_{D-j})=e_j
                                  \qquad(0\le j\le U).
                                                                    \tag{4}
\]
Let \(\mathcal L_3=R_N^{-3}\mathcal L R_N^3\) be the exact
conjugated difference operator on the full quotient. Its shortened
forcing equation is
\[
 w\mathsf F_Nf
     =\mathsf F_N(\mathcal L_3f)
            -s_m^2e_m(w)\phi_N(R_N^3fe_U),
 \qquad s_m=2\sin(\pi m/N).
                                                                    \tag{5}
\]
Since \(e_m\) is a nonzero constant multiple of \(r_N\), equation
(5) implies
\[
       \mathsf F_N(\mathcal L_3f)
           =\operatorname{rem}_{r_N}(w\mathsf F_Nf).
                                                                    \tag{6}
\]
The kernel of \(\mathsf F_N\) is therefore invariant under
\(\mathcal L_3\). Thus the induced operator on
\(\mathcal A_N/\ker\mathsf F_N\) is exactly similar, by (3), to
\[
       \mathsf M_Np=\operatorname{rem}_{r_N}(wp)
                               \quad(p\in\mathcal B_N).
                                                                    \tag{7}
\]
This is a statement about the \(m\)-dimensional quotient selected
by the actual shortened turn. It does not replace the full original
Hermite algebra by a positive algebra.

The nodes \(c_0,\ldots,c_U\) are distinct and real. Evaluation
\[
      p\longmapsto(p(c_0),\ldots,p(c_U))
                                                                    \tag{8}
\]
identifies (7) with the diagonal matrix
\(\operatorname{diag}(c_0,\ldots,c_U)\).
Equivalently, the cardinal polynomials at these nodes are its
one-dimensional eigenvectors.

## 2. Every positive self-adjoint realization is a nodal norm

Suppose a positive-definite Hermitian inner product makes the
induced operator in (7) self-adjoint. Eigenvectors belonging to
different real eigenvalues must be orthogonal. In the cardinal
basis this says precisely that there are positive numbers
\(\omega_{j,N}\) such that
\[
        \|p\|_{\omega,N}^2
                 =\sum_{j=0}^{U}\omega_{j,N}|p(c_j)|^2.
                                                                    \tag{9}
\]
Conversely every norm (9) makes (7) self-adjoint. Via (3) this
classifies all positive self-adjoint inner products on the reduced
source space, without any assumption on the conditioning of that
identification.

In particular spectral functional calculus gives
\[
       \|T_b(\mathsf M_N/2)\|_{\omega,N}\le1
                                      \qquad(b\ge0).
                                                                    \tag{10}
\]
This bound alone does not estimate the source and observation
vectors that occur in the original scalar.

Those vectors are fixed by the original finite source. Set
\[
\begin{split}
 f_{\rm full}(z)&=K_N^{\mathrm{ord}}(-2,z),\\
 \mathcal Q_N(w)&=\mathsf F_Nf_{\rm full}
   =\phi_N^{(z)}
       [R_N(z)^3K_N^{\mathrm{ord}}(-2,z)
                         K_N^{<,\mathrm{ord}}(z,w)],\\
 \beta_{j,N}&=
 (-1)^{U+j}
 \frac{s_{2j+1}S_U^2}{S_{U-j}S_{U+j+1}}\,R_N(c_j)^3 .
\end{split}                                                       \tag{11}
\]
The exact outer annihilator and radical contraction prove
\[
 \ell_N(p):=\phi_N^{(w)}[R_N(w)^3e_M(w)p(w)]
                =\sum_{j=0}^{U}\beta_{j,N}p(c_j),
                                                                    \tag{12}
\]
and hence, for the original mode response,
\[
 \mathcal L_{N,b}
      =\ell_N\!\left(T_b(\mathsf M_N/2)\mathcal Q_N\right).
                                                                    \tag{13}
\]
Every \(\beta_{j,N}\) is nonzero. Its phase retains the original
outer crossing; the inner trace in \(\mathcal Q_N\) is still full.

For a choice of (9), the dual norm of (12) and its associated
Cauchy--Schwarz cost are
\[
\begin{split}
 \|\ell_N\|_{\omega,N,*}^2
       &=\sum_{j=0}^{U}\frac{|\beta_{j,N}|^2}{\omega_{j,N}},\\
 \mathfrak C_N(\omega)
       &=\|\ell_N\|_{\omega,N,*}\|\mathcal Q_N\|_{\omega,N}.
\end{split}                                                       \tag{14}
\]
For every positive choice of weights, Cauchy--Schwarz also gives
the reverse lower estimate for this cost:
\[
 \boxed{\quad
 \mathfrak C_N(\omega)
    \ge\sum_{j=0}^{U}
              |\beta_{j,N}\mathcal Q_N(c_j)|.
 \quad}                                                           \tag{15}
\]
Moreover, the right side is the infimum of (14) over all positive
weights. If all \(\mathcal Q_N(c_j)\ne0\), equality follows by
choosing \(\omega_{j,N}=|\beta_{j,N}|/|\mathcal Q_N(c_j)|\).
At a zero component, let its weight tend to infinity and use the
same choice on the other components. This proves the infimum
statement without assuming nonvanishing at every node.

Thus optimizing the positive self-adjoint norm cannot improve
upon the sum of the absolute physical contributions. This is a
claim about the norm cost (14), not a lower bound for
\(\ell_N(\mathcal Q_N)\).

## 3. One actual physical node exceeds the required norm budget

The last node in the exact outer sum has angle
\[
 u_{U,N}=\pi-\frac{(2U+1)\pi}{N}
    =\begin{cases}\pi/N,&N\ \text{even},\\2\pi/N,&N\ \text{odd}.
      \end{cases}
                                                                    \tag{16}
\]
It is a double node at both parities. It is not the odd simple
node at angle zero, which the outer factor annihilates.

The adopted
[physical-outgoing packet](research_mixed_next_inner_three_physical_outgoing_packet.md)
applies to (16), and gives the exact inner source there:
\[
 \mathcal Q_N(c_U)
       =C_{N,3}N^{-3/2}\mathcal A(u_{U,N})
                   e^{NS(u_{U,N})}(1+O(N^{-1})),
              \qquad |C_{N,3}|=1.
                                                                    \tag{17}
\]
The coefficient is bounded away from zero. The original phase
is holomorphic and even near zero, so
\[
 S(u_{U,N})=S(0)+O(N^{-2}).
                                                                    \tag{18}
\]
The original complete degree-two theorem has the written strict
bound
\[
             \mathfrak M_3:=\Re S(0)>\frac95.
                                                                    \tag{19}
\]
Both (18) and the normalization of (19) are explicitly recorded
in equations (12)--(14) of the
[thin-strip source note](research_mixed_next_three_outer_mode_thin_strip_obstruction.md),
which traces them to the full degree-two source. Only these
already proved consequences are used; no certificate is evaluated.

The weight at the same node is only polynomially small. From
(11), with \(\theta=\pi/N\), the exact sine products give
\[
 |\beta_{U,N}|=
 \begin{cases}
 \sin\theta,&N=2m,\\[1mm]
 \displaystyle\frac{\sin(2\theta)\sin\theta}
                         {\cos^2(\theta/2)},&N=2m+1.
 \end{cases}                                                       \tag{20}
\]
Indeed \(S_U^2=N/2,\ S_{2U+1}=N\) in the even case.
In the odd case
\(S_U^2=N/(4\cos^2(\theta/2))\) and
\(S_{2U+1}=S_{N-2}=N/s_1\). Substitution into (11) proves
(20), with the crossing modulus still one.
The sine chord on \([0,\pi/2]\) gives, for sufficiently large
levels, a common lower bound \(cN^{-2}\) for (20).

Keeping this single term in (15), equations (17)--(20) imply
\[
 \boxed{\quad
 \mathfrak C_N(\omega)
       \ge cN^{-7/2}e^{N\mathfrak M_3}
       \quad\hbox{for every positive self-adjoint norm.}
 \quad}                                                           \tag{21}
\]
The constant is independent of the choice of weights. In
particular, with
\[
                  B_f=\frac{77}{50}+\frac{\pi}{50},
                                                                    \tag{22}
\]
one has, for all sufficiently large \(N\),
\[
              \mathfrak C_N(\omega)
                           \ge e^{N(B_f+1/6)}.
                                                                    \tag{23}
\]
Here is a written reserve for absorbing the polynomial in (21):
\[
       \frac95-B_f-\frac16
        >\frac95-\frac{561}{350}-\frac16
        =\frac{16}{525}>0,
                                                                    \tag{24}
\]
using \(\pi<22/7\). The original outside factor has modulus
\(1/N\), so restoring it changes no exponential conclusion.

## 4. Consequence for Jensen-weighted functional calculus

The adopted
[Jensen coefficient theorem](research_mixed_next_middle_jensen_spectral_ellipse.md)
reduces the desired sufficient estimate to
\[
 \max_{0\le b\le d}
       e^{-dI_J(b/d)}|\mathcal L_{N,b}|
                    \le C N^A e^{NB_f},
 \qquad d=U-\lfloor N/6\rfloor<N/3.
                                                                    \tag{25}
\]
The constant mode has \(I_J(0)=0\). For this mode the direct
positive functional-calculus estimate (10),(13)--(14) uses the
cost \(\mathfrak C_N(\omega)\), which satisfies (23), regardless
of how its norm is optimized. The degree-dependent weight in
(25) therefore cannot repair this particular norm argument.

This does not refute (25). It proves that the single
Cauchy--Schwarz estimate arising from any positive self-adjoint
realization of the reduced recurrence is insufficient for (25).
It does not lower-bound the signed constant response
\(\mathcal L_{N,0}\), the actual inserted trace
\(\mathcal L_N(H_N)\), or any partial angular current.

A non-self-adjoint coherent construction, an estimate that uses
the original phases before taking a positive norm, or a controlled
deformed contour may avoid this limitation. Such a construction
must retain its actual source and observation costs; the finite
operator's real eigenvalues alone do not supply the required bound.

## 5. Frozen source identifiers

The proof above uses the following unchanged source files:

- [Short-kernel operator transport](research_mixed_next_short_kernel_outer_operator_transport.md):
  \(\texttt{38df410463523eb05f3e9bed696f63bdbfda20ff03b72950a9664945d8c08068}\).
- [Exact low-edge reduction](research_mixed_next_outer_exact_low_edge_reduction.md):
  \(\texttt{76524c28bdbafafe8922993093e3e5b4447ec033e4b0dd3928295047bfde797a}\).
- [Physical-outgoing packet](research_mixed_next_inner_three_physical_outgoing_packet.md):
  \(\texttt{c43064953e7d3bfa92a6ecc05725719661e45d0b6bfca76fe1b78a28c68de4f3}\).
- [Thin-strip source normalization](research_mixed_next_three_outer_mode_thin_strip_obstruction.md):
  \(\texttt{3cc8db2cdade85a30b3ba27ee8362635e8c326fe7d02dba49182cdffb88a263a}\).
- [Original complete degree-two theorem](research_all_nonzero_degree_two_fillings.md):
  \(\texttt{7ac634d458e5805e95a7ce064d4e1fc513c96c0b758cfaee9f91fd46de10304c}\).
- [Jensen spectral coefficient theorem](research_mixed_next_middle_jensen_spectral_ellipse.md):
  \(\texttt{53e5117a9facd1793ece0ffb097bfe9f6fa4bfbb366cf6f3fc5d9c25b982ee20}\).
- [Original conjugated Askey--Wilson transport](research_current_free_aw_crossing_transport.md):
  \(\texttt{f81b9fc3edc2504c5250ad283bf0ceff191a1fc3a310c00fdb57602362f0bf4a}\).
