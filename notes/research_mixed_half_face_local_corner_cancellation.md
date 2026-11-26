# Exact cancellation of the artificial incoming half-face corner

Research deduction, 7 November 2026. A fixed short part of the
original incoming connector and the adjoining real arc can be
estimated together. Their artificial endpoint at \(a=1/2\)
cancels exactly. The complete finite source has a two-endpoint
nonstationary expansion on this short union, controlled by its
two external endpoints rather than by the removed corner.

This is a local source statement near complete ordinary color.
It neither covers the whole original incoming height interval
nor pays the resulting external endpoint against the following
affine action. No numerical evaluation is used.

## 1. Literal source, orientation, and known neighborhood

Keep the complete finite product
\[
 \begin{split}
 F_N(a,\omega,y)
 &=U_{0,N}(\omega,e^{-2\pi ia})
                  C_{1,N}(e^{-2\pi ia},e^{-2\pi iy}),\\
 U_{0,N}(\omega,X)
 &=\sum_{i=0}^{N-1}H_N(\omega,r^{-i})p_i(X)/P_i,\\
 C_{1,N}(X,Y)
 &=\sum_{j=0}^{N-1}X^{-j}p_j(X)p_j(Y)/P_j^3 .
 \end{split}                                                   \tag{1}
\]
Here \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\(p_j(X)=(rX;r)_j\). Every row, including every revived row,
and the complete endpoint polynomial \(H_N\) are retained.
For fixed \(N,\omega,y\), (1) is entire and one-periodic in \(a\).

The exact incoming contour has the successive orientations
\[
       \frac12+ih_a\longrightarrow\frac12
                         \longrightarrow 1,\qquad h_a<0.      \tag{2}
\]
This follows from the seven-segment identity in
[the complete following-prefix theorem, Section 2](research_mixed_three_four_following_complete_prefix.md).
The two vertical pieces through the original pair height
concatenate as oriented chains, even if they overlap.
The constant-mode normalization is \(N\int F_N\,da\), with
the actual complex differential. In the selected source its
remaining factors are
\[
       d_N(Y)Y^{-N}C_{\beta,N}(Y,Z),\qquad \beta\in\{0,1\},    \tag{3}
\]
with the original outgoing halfweight external to the integral.
They are independent of \(a\), so multiply every identity below
without alteration or division.

The [joint whole-source theorem](research_mixed_half_face_joint_source_packet.md)
and [incoming transport theorem](research_mixed_half_face_incoming_transport.md)
supply a fixed complex neighborhood of
\[
 \{(a,\omega)=(1/2,-2)\}\times
 \mathcal Y,\qquad
 \mathcal Y=[11/50,9/20]+i[0,1/100],
                                                                  \tag{4}
\]
on which
\[
 F_N=N^{-2}\mathcal A_N e^{N\mathcal P},\qquad
 \mathcal A_N=\mathcal D(1+O_{\rm hol}(N^{-1})),\qquad
 \mathcal D\ne0,\qquad \Re\mathcal P_a<-2/5 .                \tag{5}
\]
All phases, additive constants, coefficients, and both parities
are the original ones. Equation (5) is a packet for the whole
finite product, not for only its two retained saddle integrals.
On a smaller fixed neighborhood, \(\mathcal A_N\) and all its
fixed derivatives are uniformly bounded.

## 2. A uniform local phase chart

Write \(a_c=1/2\), and let \(\zeta=(\omega,y)\) denote the
outside parameters. After shrinking the neighborhood in (4),
there is a common radius \(\rho>0\) such that
\[
 a\longmapsto
          \mathcal P(a,\zeta)-\mathcal P(a_c,\zeta)           \tag{6}
\]
is injective on \(|a-a_c|<\rho\), and its image contains a
fixed disk \(|s|<\rho_1\), uniformly for \(\zeta\) in a
fixed neighborhood of \(\{-2\}\times\mathcal Y\).
Its inverse \(a=\chi_\zeta(s)\) is holomorphic jointly in
the parameters and \(s\).

Here no global inverse assertion is needed. For a direct
uniform proof, (5) bounds \(|\mathcal P_a(a_c,\zeta)|\)
away from zero. Uniform continuity of the derivative allows
\(\rho\) so small that
\[
 |\mathcal P_a(a,\zeta)-\mathcal P_a(a_c,\zeta)|
                 <\tfrac12|\mathcal P_a(a_c,\zeta)|
                   \quad(|a-a_c|\le\rho).                  \tag{7}
\]
Integrating the difference along any segment in the disk
proves injectivity. The same estimate on its boundary,
or the elementary Rouché argument comparing (6) with
\(\mathcal P_a(a_c,\zeta)(a-a_c)\), gives a uniform image
disk. The analytic inverse theorem then proves the asserted
joint holomorphy. Compactness of (4) makes these choices uniform.

Choose fixed small \(\epsilon,\ell>0\) so that
\[
        A=\frac12-i\epsilon,\qquad B=\frac12+\ell            \tag{8}
\]
and the original broken path \(A\to a_c\to B\) lie in this
neighborhood, and the two values in (6) at \(A,B\) lie in
\(|s|<\rho_1/2\). Their straight joining segment lies in
the same phase disk. Its inverse under \(\chi_\zeta\)
is an allowed path from \(A\) to \(B\), of uniformly
bounded length. Along this path,
\[
 \Re\mathcal P(a,\zeta)\le
       M_{AB}(\zeta):=
       \max\{\Re\mathcal P(A,\zeta),\Re\mathcal P(B,\zeta)\}.
                                                                  \tag{9}
\]
The literal source (1) is entire, so the integral on the
broken path equals its integral on this new path exactly.
This uses finite-source holomorphy in a neighborhood already
covered by (5), not merely the continued algebraic critical phase.

## 3. Complete two-endpoint expansion

Define the original normalized local union
\[
 I_N^{\rm corner}(\zeta)=
 N\left\{\int_A^{a_c}F_N(a,\zeta)\,da+
                  \int_{a_c}^{B}F_N(a,\zeta)\,da\right\}.
                                                                  \tag{10}
\]
There is a holomorphic remainder \(\mathcal R_N\) such that
\[
 \boxed{\quad
 I_N^{\rm corner}
  =N^{-2}\left[
       \frac{\mathcal D(a,\zeta)}{\mathcal P_a(a,\zeta)}
                         e^{N\mathcal P(a,\zeta)}
                      \right]_{a=A}^{a=B}
                      +\mathcal R_N(\zeta),\qquad
 |\mathcal R_N|\le C N^{-3}e^{N M_{AB}} .
 \quad}                                                        \tag{11}
\]
This is uniform on fixed smaller outside-parameter neighborhoods
and for both parities. For each fixed total derivative order \(k\)
in the outside parameters one also has
\[
               |\partial^k\mathcal R_N|
                      \le C_kN^{k-3}e^{N M_{AB}}.             \tag{12}
\]
An arbitrarily small additional exponential tolerance can instead
absorb these polynomial derivative costs.

To prove (11), use the path of Section 2 and put
\[
 B_{0,N}=\mathcal A_N/\mathcal P_a,\qquad
 B_{1,N}=(\partial_a B_{0,N})/\mathcal P_a .
 \]
The functions and the derivatives used here are uniformly
bounded on the fixed compact chart, by (5), (7).
Two integrations by parts give the exact identity
\[
 \begin{split}
 I_N^{\rm corner}
   ={}&N^{-2}[B_{0,N}e^{N\mathcal P}]_A^B
        -N^{-3}[B_{1,N}e^{N\mathcal P}]_A^B\\
     &+N^{-3}\int_A^B
                       \partial_aB_{1,N}\,e^{N\mathcal P}\,da .
 \end{split}                                                   \tag{13}
\]
The last integral is along the allowed phase path. Its bounded
length and (9) give \(O(N^{-3}e^{NM_{AB}})\). Replacing
\(\mathcal A_N\) by \(\mathcal D\) in the first endpoint
term costs the same amount, proving (11).

The original broken contour in (10) is fixed, so its integral
and the remainder in (11) are holomorphic in the outside
variables. The endpoint phase maximum varies by \(O(1/N)\)
on outside polydisks of radius \(O(1/N)\), with a uniform
constant. Cauchy's formula applied to (11)'s remainder bound
therefore proves (12). This does not treat \(M_{AB}\) as a
holomorphic normalization.

Alternatively perform the first integration by parts on the
two original pieces separately. At their common endpoint,
the upward connector contributes
\[
       +N^{-2}B_{0,N}(a_c,\zeta)e^{N\mathcal P(a_c,\zeta)},
\]
and the rightward real arc contributes precisely its negative.
The two terms cancel with their exact finite amplitudes,
before replacing \(\mathcal A_N\) by its leading symbol.
The same cancellation holds at every further integration
by parts. It is compatible with the nonzero one-sided
endpoint term in the earlier incoming integral theorem.

## 4. External endpoints and remaining scope

The right endpoint has the proved local decrease
\[
 \Re\mathcal P(B,\zeta)
       \le\Re\mathcal P(a_c,\zeta)-2\ell/5,                  \tag{14}
\]
as long as the selected horizontal segment remains in (5).
No analogous sign for the lower endpoint \(A\) is assumed.
Equation (11) proves that the artificial phase value at
\(a_c\) need not enter an upper estimate for this local union:
only the two external phase values remain. Their two
nonzero coefficients need not have a nonzero difference.

For a particular original connector, its top subsegment
in (10) exists only if \(\epsilon\le-h_a\). If the actual
connector is shorter, its lower endpoint itself can be used,
provided it lies in the same fixed chart; (11) remains
uniform for such endpoints. This does not enlarge the
chart to cover an arbitrary actual height in (2).

The remaining long vertical piece, the external lower
endpoint's action, and a comparison with the full following
affine action are not paid here. A deformation of the whole
union from \(1/2+ih_a\) to a distant real endpoint would
require finite-source control on the entire displaced path.
The already proved phase continuation and real-arc upper
bound alone do not provide that control. All statements
here concern complete color and its fixed local complex
neighborhood; no remote real-color packet, individual
Fourier-sector suppression, or filled-source conclusion
is inferred.
