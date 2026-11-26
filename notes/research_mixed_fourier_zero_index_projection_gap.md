# The zero-index projection is exponentially small near the Fourier reference

Research consequence, 7 November 2026. The exact projection onto the
first Fourier basis vector has a strict exponential gap below the
complete boundary function near its actual reference. This gives a
controlled use of the boundary lowering operator without its endpoint
term on this particular analytic section. The statement is local and
does not assert the same gap after applying a short crossing.

## 1. The projection is a specific original seam value

Use the complete finite function and the Fourier basis from
[the full asymptotic theorem](research_mixed_fourier_right_cap_full_asymptotic.md):
\[
 \begin{split}
 Z_N(a,y)&=V_N^{\rm F}(y,X)
       =\sum_{l=0}^{N-1}C_{1,N}(X,r^l)f_l(y),\\
 X&=e^{-2\pi ia},\qquad Y=e^{2\pi iy},\qquad r=e^{-2\pi i/N},\\
 f_l(y)&=\frac{e^{-\pi i(N-1)y}}N
       Y^l\prod_{k=l+1}^{N-1}(1-Yr^k).
 \end{split}
 \tag{1}
\]
On this Fourier band, the mark \(\mathsf E_Z\) in the
[exact difference system](research_mixed_fourier_exact_boundary_difference_system.md)
has \(\mathsf E_Zf_l=r^{-l}f_l\). Therefore
\[
 \mathsf P_0=\frac1N\sum_{k=0}^{N-1}\mathsf E_Z^k,
 \qquad
 \mathsf P_0 Z_N=f_0(y)C_{1,N}(X,1).
 \tag{2}
\]
This is an exact finite projection, at both level parities. It does
not project onto a stationary point or an asymptotic branch.
Although its operator formula uses shifts through a full period,
the estimate below uses the exact seam value in (2); it does not
apply those shifts to an asymptotic known only near one point.

Fix one actual reference \((a_0,y_0)=(a_0,x_0)\), with incoming
flag \(\eta\in\{0,1\}\), and put \(c=\Im a_0\).
The original supporting-plane rate \(B_\eta(x)\) satisfies
\[
 B_\eta(\Re a_0)=\Re\Phi(a_0,y_0)
                               -\frac\eta2\Re g(a_0),
 \tag{3}
\]
where \(\Phi\) is the selected action of the complete function.

Equation (29) of
[the real-seam contour theorem](research_mixed_fourier_real_seam_contour.md)
proves, eventually and uniformly for \(x\in P=[.22,.45]\),
\[
 |d_N(e^{-2\pi i(x+ic)})|^{\eta/2}
 |f_0(y_0)C_{1,N}(e^{-2\pi i(x+ic)},1)|
 \le e^{N\{B_\eta(x)-\delta_0\}},
 \qquad \delta_0=\frac1{140000}.
 \tag{4}
\]
The two-function premise retained in that earlier note has been
discharged by
[the left-taper completion](research_mixed_fourier_left_taper_completion.md).
The separately bounded high physical rows in (4) are essential;
the estimate is for the entire conditional factor at its physical
outgoing endpoint, not just its low-index part.

## 2. A fixed complex neighborhood preserves the gap

**Theorem.** There are a fixed complex neighborhood \(U\) of
\((a_0,y_0)\), a constant \(\gamma>0\), and \(N_0\) such that
\[
       |\mathsf P_0Z_N(a,y)|
           \le e^{N\{\Re\Phi(a,y)-\gamma\}}
                    \qquad((a,y)\in U,\ N\ge N_0).
 \tag{5}
\]
On smaller neighborhoods, every fixed derivative of
\[
 \frac{\mathsf P_0Z_N(a,y)}{N^{-3/2}\mathcal A(a,y)e^{N\Phi(a,y)}}
 \quad\hbox{and}\quad
 \frac{\mathsf P_0Z_N(a,y)}{Z_N(a,y)}
 \tag{6}
\]
is exponentially small in \(N\). Here \(\mathcal A\ne0\)
is the original coefficient of the complete holomorphic asymptotic.

*Proof.* Put
\(F_N(a)=f_0(y_0)C_{1,N}(e^{-2\pi ia},1)\).
The function
\[
                 d_N(e^{-2\pi ia})^\eta F_N(a)^2
 \tag{7}
\]
is a Laurent polynomial in \(e^{-2\pi ia}\) with exponent
band bounded by \(2N\) in absolute value. Its modulus is
exactly the square of the left side of (4), including at zeros.
The [horizontal complex extension theorem](research_mixed_horizontal_complex_extension.md)
therefore applies to its continuous rate
\(2B_\eta(x)-2\delta_0\). For any fixed \(\epsilon>0\)
there is a neighborhood of \(a_0\) on which
\[
 |d_N(e^{-2\pi ia})|^{\eta/2}|F_N(a)|
 \le C N^A
     e^{N\{B_\eta(\Re a_0)-\delta_0+\epsilon\}}.
 \tag{8}
\]
One uses the theorem at the real center \(\Re a_0\), whose
height is \(c\). This argument does not estimate the derivative
of a finite-level value by continuity alone.

For \(\eta=1\), restrict the neighborhood to the interior
of the original zero-free \(E_4\) rectangle. The proved incoming
weight asymptotic gives, uniformly there,
\[
 |d_N(e^{-2\pi ia})|^{-1/2}
                  \le C' N^{1/4}e^{N\Re g(a)/2}.
 \tag{9}
\]
This is the same legitimate weight removal used in the complete
holomorphic packet. No division is made at a weight zero on a
larger interval. For \(\eta=0\), no weight removal is needed.

The output dependence of the projection has an especially simple
exact form:
\[
                  f_0(y)=\frac{e^{-\pi i(N-1)y}}N
                                 \frac{1-Y^N}{1-Y}.
 \tag{10}
\]
On a sufficiently small neighborhood of \(y_0\), the modulus
of \(Y\) is bounded above by a fixed number less than one,
and \(1-Y\) is bounded away from zero. Consequently
\[
 \left|\frac{f_0(y)}{f_0(y_0)}\right|
       \le C'' e^{\pi N(\Im y-\Im y_0)}.
 \tag{11}
\]
All omitted factors here are uniformly bounded; \(f_0(y_0)\)
is nonzero at every level. Equations (2), (8)--(11) bound the
projection by a polynomial factor times the exponential with rate
\[
 B_\eta(\Re a_0)+\frac\eta2\Re g(a)
          +\pi(\Im y-\Im y_0)-\delta_0+\epsilon.
 \tag{12}
\]
At the center, the first three terms equal \(\Re\Phi(a_0,y_0)\)
by (3). Their difference from \(\Re\Phi(a,y)\) is continuous.
Choose \(\epsilon<\delta_0/8\), shrink the fixed neighborhood
so that this difference has modulus less than \(\delta_0/8\),
and absorb the polynomial factor into a further fixed fraction
of \(\delta_0\). This proves (5), for example with a smaller
gap \(\gamma=\delta_0/2\).

The normalized functions in (6) are holomorphic on a smaller
neighborhood. The first denominator has nonzero \(\mathcal A\);
the second is nonzero for all sufficiently large levels by the
[complete holomorphic packet](research_mixed_fourier_right_cap_holomorphic_packet.md).
Its relative error is uniformly \(O(N^{-1})\).
Equation (5), followed by Cauchy's estimates on nested
neighborhoods, proves the asserted exponential fixed-derivative
bounds, after another decrease of the gap. \(\square\)

## 3. The endpoint term in the lowering operator

Define \(\mathsf Bf_l=f_{l-1}\) for \(l\ge1\), and
\(\mathsf Bf_0=0\). Directly from (1),
\[
 \mathsf B=(Y^{-1}-\mathsf E_Z^{-1})(I-\mathsf P_0)
                         \quad\hbox{on the finite Fourier band}.
 \tag{13}
\]
The inverse mark exists on that band, since its eigenvalues
are nonzero. The projection is indispensable in this exact
identity: on its range,
\[
 (Y^{-1}-\mathsf E_Z^{-1})f_0
       =(Y^{-1}-1)f_0
       =\frac{e^{-\pi i(N-1)y}}{NY}(1-Y^N),
 \tag{14}
\]
which is not the zero function.

Nevertheless, for the original \(Z_N\), the difference between
the two expressions obtained with and without \(I-\mathsf P_0\)
in (13) is exactly
\[
                         (Y^{-1}-1)\mathsf P_0Z_N.
 \tag{15}
\]
The multiplier is bounded and holomorphic near the actual output.
The theorem therefore bounds this particular correction, with
all fixed normalized derivatives, strictly below the complete
source's exponential rate.

This conclusion neither estimates \(\mathsf E_Z^{-1}Z_N\)
separately nor justifies iterating (13) without its endpoint
projection. After a crossing, the projected coefficient belongs
to a different source and needs its own bound. The exact crossing
and closing operations are retained in
[the original closing interface](research_mixed_fourier_boundary_closing_interface.md).
The full-period closing estimate and short-filling stability
remain open.
