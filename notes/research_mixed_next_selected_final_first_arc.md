# The final real first-coordinate arc of the selected next source

Research deduction, 7 November 2026. The complete original source on
the real first-coordinate arc \([13/16,1]\) is exponentially smaller
than the ordinary-next affine action when the second coordinate ranges
over its entire selected plateau. This is an estimate of an actual
continuous contour segment. It does not use physical termination
away from the root grid, or replace the full prefix by its cardinal
filter.

## 1. An exact quotient maximum on the final real arc

Use \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(p_j(X)=(rX;r)_j\), and the continuous one-periodic primitive
\[
 J(t)=\int_0^t\log(2|\sin\pi u|)\,du,\qquad J(0)=J(1)=0.
                                                               \tag{1}
\]
Thus \(J(-t)=-J(t)\). For \(0\le v\le1/2\), set
\[
 A(v)=J(v)-2J(v/2).
                                                               \tag{2}
\]

**Lemma 1.** Uniformly for \(0\le t\le1\),
\[
 I_{1-v}(t)-J(t)
   :=J(t-v)+J(v)-J(t)\le A(v),\qquad
       0\le A(v)\le v\log2 .
                                                               \tag{3}
\]

*Proof.* For \(0<v\le1/2\), differentiation with respect to \(t\),
away from its integrable logarithmic singularities, gives
\[
 \partial_t[I_{1-v}(t)-J(t)]
       =\log\frac{|\sin\pi(t-v)|}{\sin\pi t}.
                                                               \tag{4}
\]
The difference of the squared numerator and denominator is
\(-\sin\pi v\,\sin\pi(2t-v)\). The expression in (3) therefore
increases to \(t=v/2\), decreases to \(t=(1+v)/2\), then
increases to \(t=1\). Its endpoint values are zero, and its
first local maximum is \(A(v)\). The integral is continuous
through its singularities. Finally,
\[
 A'(v)=\log(2\cos(\pi v/2)),\qquad A(0)=0.
                                                               \tag{5}
\]
This derivative is positive on \([0,1/2]\) and at most
\(\log2\). This proves (3), including \(v=0\). \(\square\)

The zero-safe finite-product upper estimate and the uniform
denominator factorial estimate, as stated in
[the continuous far-half cap theorem](research_mixed_three_four_continuous_far_half_cap.md),
Section 1, consequently give
\[
 \frac{|p_j(e^{-2\pi i(1-v)})|}{|P_j|}
       \le C_\tau N^{B_\tau}e^{N\{A(v)+\tau\}},
       \qquad 0\le j<N.                                    \tag{6}
\]
The estimate includes \(j=0,N-1\), the point \(v=0\),
and every numerator zero. It is valid between physical roots.

## 2. The whole cap and conditional polynomial

Keep the literal finite factors
\[
 \begin{split}
 U_{0,N}(w,X)&=\sum_{j<N}
                H_N(w,r^{-j})\,p_j(X)/P_j,\\
 C_{1,N}(X,Y)&=\sum_{j<N}
                X^{-j}p_j(X)p_j(Y)/P_j^3.
 \end{split}                                                 \tag{7}
\]
Every \(H_N\) in (7) is the complete endpoint polynomial.
The all-real extension of
[the coherent seam bound](research_mixed_cap_seam_source_bounds.md),
as used in
[the complementary real-color theorem](research_mixed_three_four_complementary_real_colors.md),
gives
\[
 \sum_{j<N}|H_N(w,r^{-j})|
       \le C_\tau N^{B_\tau}e^{N(101/125+\tau)}
          \qquad(-2\le w\le2).                              \tag{8}
\]
The same estimate with an arbitrarily small extra allowance holds
on a sufficiently small fixed disk about \(w=-2\).

The centered-arc bound and the polynomial maximum principle give
\[
 |p_j(Y)|\le C_\tau N^{B_\tau}e^{N\{L(j/N)+\tau\}},
 \quad |Y|\le1,\qquad L(t)=-2J((1-t)/2).
                                                               \tag{9}
\]
The existing complete scalar bound is
\[
            \max_{0\le t\le1}[L(t)-2J(t)]<7/15.
                                                               \tag{10}
\]
Equations (9)--(10) are the whole-index estimates in Section 3
of the continuous far-half cap theorem, not a compact-row
asymptotic.

For \(a=1-v\) real, \(|X^{-j}|=1\). Applying (6) to
the incoming numerator of each factor in (7), then using
(8)--(10), yields
\[
 \begin{split}
 |U_{0,N}(w,X)|
       &\le C_\tau N^{B_\tau}
                   e^{N\{101/125+A(v)+\tau\}},\\
 \sup_{|Y|\le1}|C_{1,N}(X,Y)|
       &\le C_\tau N^{B_\tau}
                   e^{N\{7/15+A(v)+\tau\}}.
 \end{split}                                                 \tag{11}
\]
These estimates take no modulus inside an endpoint Newton sum.
The positive sum over the conditional rows retains every original
finite product and denominator.

For \(0\le v\le3/16\), (3) and \(\log2<7/10\) imply
\[
 \frac{101}{125}+2A(v)+\frac7{15}
       <\frac{101}{125}+\frac{21}{80}+\frac7{15}
        =\frac{9223}{6000}
        =\frac{77}{50}-\frac{17}{6000}.                     \tag{12}
\]
One can therefore choose the total finite/color tolerance
strictly below \(17/6000\) and obtain the useful whole-disk bound
\[
 \sup_{\substack{13/16\le a\le1\\ |Y|\le1\\ -2\le w\le2}}
       |U_{0,N}(w,e^{-2\pi ia})
                        C_{1,N}(e^{-2\pi ia},Y)|
                 \le C N^B e^{77N/50}.                     \tag{13}
\]
It also holds on a sufficiently small fixed complex color disk.
Both level parities are included. The exact chirp has modulus
one here; it has not been dropped on a nonreal incoming path.

## 3. Payment on the entire selected second plateau

Use exactly the ordinary-next reference, bare action, and affine
plane \(\Lambda_{123}\) of
[the filtered selected-plateau theorem](research_mixed_next_filtered_selected_plateau.md),
equations (3)--(8). In particular the first three flags are
\((0,1,\beta)\), \(\beta=0,1\), both conditional indices
are ordinary, and the external parameter is
\(s_4^*\in K_3\cup K_4\). Put
\[
 y=x+i/100,\quad x\in P=[.22,.45],\qquad
 z=u+i\Im z_*,\quad u\in P,\qquad
 Y=e^{-2\pi iy},\ Z=e^{-2\pi iz}.
                                                               \tag{14}
\]

The proof in Sections 3--4 of that theorem applies to any
degree-\(D\) polynomial in \(Y\) with the whole-disk bound
\(C N^B e^{77N/50}\). Its only uses of the cardinal correction
were that degree and that bound. Equation (13) supplies them
pointwise in \(a\) for the complete original product \(U_0C_1\).
Its two remaining inputs are unchanged:
\[
 \begin{split}
 |d_N(Y)Y^{-N}|^{1/2}
 &\le C_\tau N^{B_\tau}
   e^{N\{\max(-J(x)/2-3\pi/400,0)+\tau\}},\\
 |C_{\beta,N}(Y,Z)|\,|d_N(Y)Y^{-N}|^{1/2}
                       |d_N(Z)|^{\beta/2}
 &\le C_\tau N^{B_\tau}e^{N\{B_3(x,u)+7/250+\tau\}}.
 \end{split}                                                 \tag{15}
\]
The first line retains both the factorial and the polynomial
forcing alternative of the exact Fourier weight. The second is
the complete ordinary third-factor bound with its original
supporting plane, all rows, aliases and joins. The actual first-pair
marginal cancels its incoming tangent exactly.

**Theorem 2.** For every prescribed sufficiently small \(\tau>0\),
\[
 \begin{split}
 &|U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)Y^{-N}
                            C_{\beta,N}(Y,Z)|
                              |d_N(Z)|^{\beta/2}\\
 &\hspace{20mm}\le C_\tau N^{B_\tau}
                  e^{N\{\Lambda_{123}(z)-1/500+\tau\}},
       \qquad a\in[13/16,1],
 \end{split}                                                 \tag{16}
\]
uniformly on (14) and the stated ordinary-next reference family,
at all real ordinary colors and both parities.
For \(\beta=0\), no outgoing halfweight is inserted.
After finite tolerances and polynomial factors, the loss may be
taken to be \(1/1000\).

*Proof.* Apply the degree-\(D\) disk extension to (13), giving
the selected-radius cost \(\pi/50\), then multiply the two
bounds (15). The exact comparison with
\(\Lambda_{123}\) is the two-sign marginal calculation
(18)--(31) of the filtered selected-plateau theorem.
It has raw reserve greater than \(1/500\) uniformly in
\(x\in P\). No first-coordinate saddle or cap profile is
substituted for (7). \(\square\)

Define the actual final-arc contribution to the complete prefix by
\[
 F_{34,N}^{\mathrm{end}}(w,Y)
   =N\int_{13/16}^{1}U_{0,N}(w,e^{-2\pi ia})
                         C_{1,N}(e^{-2\pi ia},Y)\,da .
                                                               \tag{17}
\]
It is a polynomial of degree at most \(D\) in \(Y\).
Multiplication by the exact remaining selected factors, and
integration over \(P+i/100\), preserves (16); both original
factors \(N\) cost only polynomial powers. This is a part of
the original continuous two-coordinate contour.

Fixed real ordinary-color derivatives follow by Markov applied
to each complete \(H_N\) before the positive sum in (8).
Small complex color neighborhoods use their already allowed
tolerance. For fixed local mixed derivatives, keep both integration
segments fixed at a base reference and use the strict rate reserves
on smaller parameter neighborhoods. Near the actual outgoing
reference the original nonzero type-four weight, if present, permits
the same local normalization as the filtered selected-plateau proof;
Cauchy's formula gives its conservative \(1/2000\) normalized
derivative loss. No division through a Fourier-weight zero at a
general plateau target is asserted.

The real interval \([1/2,13/16]\) and the initial vertical
connector of the first-coordinate complement remain outside
this theorem. The estimate concerns neither a subset of physical
roots nor a complete Fourier coefficient.
